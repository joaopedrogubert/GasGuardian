import sqlite3
from entidades.tipoCombustivel import TipoCombustivel
from entidades.tanqueCombustivel import TanqueCombustivel
from entidades.bombaCombustivel import BombaCombustivel

class ControladorBombaCombustivel:
    def __init__(self):
        self.conn = sqlite3.connect('/Users/railanabreu/Documents/Projects/GasGuardian/Raillan/dados/DADOS.sqlite')
        self.cursor = self.conn.cursor()
        self.conn.commit()

    def adicionar_bomba(self, autoAbastecimento, tipoCombustivel, bombaAtiva, tanque, nomeBomba):
        nova_bomba = BombaCombustivel(autoAbastecimento, tipoCombustivel, bombaAtiva, tanque, nomeBomba)
        try:
            with self.conn:
                self.cursor.execute(
                    "INSERT INTO Bombas (autoAbastecimento, tipoCombustivel_nome, bombaAtiva, tanque_id, nomeBomba) VALUES (?, ?, ?, ?, ?)",
                    (nova_bomba.autoAbastecimento, nova_bomba.tipoCombustivel[0].nome, nova_bomba.bombaAtiva, nova_bomba.tanque.id, nova_bomba.nomeBomba)
                )
                self.conn.commit()
        except sqlite3.IntegrityError as e:
            raise ValueError(f"Erro ao adicionar bomba: {e}")

    def listar_bombas(self):
        self.cursor.execute("""
            SELECT b.id, b.autoAbastecimento, b.tipoCombustivel_nome, b.bombaAtiva, t.nome AS tanque_nome, b.nomeBomba
            FROM Bombas b
            JOIN Tanques t ON b.tanque_id = t.id
        """)
        bombas = self.cursor.fetchall()

        bombas_atualizadas = []
        for bomba in bombas:
            id, autoAbastecimento, tipoCombustivel_nome, bombaAtiva, tanque_nome, nomeBomba = bomba
            bomba_atualizada = (nomeBomba , autoAbastecimento, tipoCombustivel_nome, bombaAtiva, tanque_nome,id )
            bombas_atualizadas.append(bomba_atualizada)
        
        return bombas_atualizadas

    def buscar_bomba(self, identificadorBomba):
        self.cursor.execute("SELECT * FROM Bombas WHERE id = ?", (identificadorBomba,))
        return self.cursor.fetchone()

    def remover_bomba(self, identificadorBomba):
        try:
            with self.conn:
                self.cursor.execute("DELETE FROM Bombas WHERE id = ?", (identificadorBomba,))
                return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            return e

    def atualizar_bomba(self, autoAbastecimento, tipoCombustivel, bombaAtiva, tanque, nomeBomba, identificadorBomba):
        try:
            with self.conn:
                update_query = "UPDATE Bombas SET"
                update_values = []
                if autoAbastecimento is not None:
                    update_query += " autoAbastecimento = ?,"
                    update_values.append(autoAbastecimento)
                if tipoCombustivel is not None:
                    update_query += " tipoCombustivel_nome = ?,"
                    update_values.append(tipoCombustivel.nome)
                if bombaAtiva is not None:
                    update_query += " bombaAtiva = ?,"
                    update_values.append(bombaAtiva)
                if tanque is not None:
                    update_query += " tanque_id = ?,"
                    update_values.append(tanque.id)
                if nomeBomba is not None:
                    update_query += " nomeBomba = ?,"
                    update_values.append(nomeBomba)
                update_query = update_query.rstrip(",") + " WHERE id = ?"
                update_values.append(identificadorBomba)
                self.cursor.execute(update_query, update_values)
                self.conn.commit()
                if self.cursor.rowcount > 0:
                    print("Bomba atualizada com sucesso!")
                    return True
                else:
                    print("Nenhuma bomba encontrada com o identificador fornecido.")
                    return False
        except sqlite3.Error as e:
            print(f"Erro ao atualizar a bomba: {e}")
            return False

    def __del__(self):
        self.conn.close()
