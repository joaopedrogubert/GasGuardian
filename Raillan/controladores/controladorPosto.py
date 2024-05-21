import sqlite3
from ..entidades.posto import PostoGasolina

class ControladorPosto:
    def __init__(self):
        # Conectar ao banco de dados
        self.conn = sqlite3.connect('/Users/railanabreu/Documents/Projects/GasGuardian/Raillan/dados/DADOS.sqlite')
        self.cursor = self.conn.cursor()
        self.__posto = PostoGasolina
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Postos (
            cnpj TEXT PRIMARY KEY,
            chavePix TEXT UNIQUE,
            nomePosto TEXT NOT NULL)
    ''')
        self.conn.commit()

    @property
    def posto(self):
        return self.__posto
    

    def adicionar_posto(self, posto):
        if not isinstance(posto, PostoGasolina):
            raise ValueError("O objeto fornecido não é uma instância da classe Posto.")

        try:
            with self.conn:
                self.cursor.execute("INSERT INTO Postos (cnpj, chavePix, nomePosto) VALUES (?, ?, ?)",
                                    (posto.cnpj, posto.chavePix, posto.nomePosto))
                self.conn.commit()
        except sqlite3.IntegrityError as e:
            # Se houver uma violação de integridade (como chave duplicada), lança uma exceção
            if 'UNIQUE constraint failed: Postos.cnpj' in str(e):
                raise ValueError("Erro: CNPJ já cadastrado.")
            elif 'UNIQUE constraint failed: Postos.chavePix' in str(e):
                raise ValueError("Erro: Chave PIX já cadastrada.")
            else:
                raise

    def listar_postos(self):
        # Listar todos os postos do banco de dados
        self.cursor.execute("SELECT * FROM Postos")
        return self.cursor.fetchall()

    def buscar_posto(self, cnpj):
        # Buscar um posto específico pelo CNPJ
        self.cursor.execute("SELECT * FROM Postos WHERE cnpj = ?", (cnpj,))
        return self.cursor.fetchone()

    def remover_posto(self, cnpj):
        # Remover um posto pelo CNPJ
        with self.conn:
            self.cursor.execute("DELETE FROM Postos WHERE cnpj = ?", (cnpj,))
            return self.cursor.rowcount > 0  # Retorna True se um posto foi removido

    def atualizar_posto(self, posto):
        if not isinstance(posto, PostoGasolina):
            raise ValueError("O objeto fornecido não é uma instância da classe PostoGasolina.")
        try:
            with self.conn:
                self.cursor.execute(
                    "UPDATE Postos SET chavePix = ?, nomePosto = ? WHERE cnpj = ?",
                    (posto.chavePix, posto.nomePosto, posto.cnpj)
                )
                self.conn.commit()  # Garantir que as mudanças sejam salvas
                if self.cursor.rowcount > 0:
                    print("Posto atualizado com sucesso!")
                    return True
                else:
                    print("Nenhum posto encontrado com o CNPJ fornecido.")
                    return False
        except sqlite3.Error as e:
            print(f"Erro ao atualizar o posto: {e}")
            return False

    def __del__(self):
        # Fechar a conexão com o banco de dados
        return self.conn.close()