from entidades.bombaCombustivel import BombaCombustivel
import sqlite3

class ControladorBombaCombustivel:
    def __init__(self):
        self.conn = sqlite3.connect('/Users/railanabreu/Documents/Projects/GasGuardian/Raillan/dados/DADOS.sqlite')
        self.cursor = self.conn.cursor()
        self.__bomba = BombaCombustivel
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Bombas (
            IdentificadorBomba INTEGER PRIMARY KEY AUTOINCREMENT,
            autoAbastecimento BOOLEAN NOT NULL,
            tipoCombustivel TEXT NOT NULL,
            bombaAtiva BOOLEAN NOT NULL)
    ''')
            
        self.conn.commit()
        
    @property
    def nova_bomba(self):
        return self.__bomba
    
    def adicionar_bomba(self, autoAbastecimento, tipoCombustivel, bombaAtiva):
        nova_bomba = BombaCombustivel(autoAbastecimento, tipoCombustivel, bombaAtiva)
        if not isinstance(nova_bomba, BombaCombustivel):
            raise ValueError("O objeto fornecido não é uma instância da classe BombaCombustivel.")
        try:
            with self.conn:
                self.cursor.execute("INSERT INTO Bombas (autoAbastecimento, tipoCombustivel, bombaAtiva) VALUES (?, ?, ?)",
                                    (nova_bomba.autoAbastecimento, nova_bomba.tipoCombustivel, nova_bomba.bombaAtiva))
                self.conn.commit()
        except sqlite3.IntegrityError as e:
            # Se houver uma violação de integridade (como chave duplicada), lança uma exceção
            if 'UNIQUE constraint failed: Bombas.autoAbastecimento' in str(e):
                raise ValueError("Erro: Auto Abastecimento já cadastrado.")
            elif 'UNIQUE constraint failed: Bombas.tipoCombustivel' in str(e):
                raise ValueError("Erro: Tipo de Combustível já cadastrado.")
            else:
                raise

    def listar_bombas(self):
        # Listar todas as bombas do banco de dados
        self.cursor.execute("SELECT * FROM Bombas")
        return self.cursor.fetchall()
    
    def buscar_bomba(self, identificadorBomba):
        # Buscar uma bomba específica pelo Identificador
        self.cursor.execute("SELECT * FROM Bombas WHERE IdentificadorBomba = ?", (identificadorBomba,))
        return self.cursor.fetchone()
    
    def remover_bomba(self, identificadorBomba):
        # Remover uma bomba pelo Identificador
        with self.conn:
            self.cursor.execute("DELETE FROM Bombas WHERE IdentificadorBomba = ?", (identificadorBomba,))
            return self.cursor.rowcount > 0
        
    def atualizar_bomba(self, identificadorBomba, autoAbastecimento, tipoCombustivel, bombaAtiva):
        nova_bomba = BombaCombustivel(autoAbastecimento, tipoCombustivel, bombaAtiva)
        if not isinstance(nova_bomba, BombaCombustivel):
            raise ValueError("O objeto fornecido não é uma instância da classe BombaCombustivel.")
        try:
            with self.conn:
                self.cursor.execute("UPDATE Bombas SET autoAbastecimento = ?, tipoCombustivel = ?, bombaAtiva = ? WHERE IdentificadorBomba = ?",
                                    (nova_bomba.autoAbastecimento, nova_bomba.tipoCombustivel, nova_bomba.bombaAtiva, identificadorBomba))
                self.conn.commit()
        except sqlite3.IntegrityError as e:
            # Se houver uma violação de integridade (como chave duplicada), lança uma exceção
            if 'UNIQUE constraint failed: Bombas.autoAbastecimento' in str(e):
                raise ValueError("Erro: Auto Abastecimento já cadastrado.")
            elif 'UNIQUE constraint failed: Bombas.tipoCombustivel' in str(e):
                raise ValueError("Erro: Tipo de Combustível já cadastrado.")
            else:
                raise

    @property
    def nova_bomba(self):
        return self.__bomba
    
    @nova_bomba.setter
    def nova_bomba(self, value):
        self.__bomba = value

    def __del__(self):
        self.conn.close()


