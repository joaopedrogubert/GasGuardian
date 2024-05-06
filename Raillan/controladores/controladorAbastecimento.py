from ..entidades.abastecimento import Abastecimento
import sqlite3

class ControladorAbastecimento:
    def __init__(self):
        self.conn = sqlite3.connect('/Users/railanabreu/Documents/Projects/gas-guardian/Raillan/dados/dadosTanqueCombustivel.sqlite')
        self.cursor = self.conn.cursor()
        self.__abastecimento = Abastecimento
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Abastecimentos (
            IdentificadorAbastecimento INTEGER PRIMARY KEY AUTOINCREMENT,
            IdentificadorBomba INTEGER NOT NULL,
            data TEXT NOT NULL,
            litros REAL NOT NULL,
            valorTotal REAL NOT NULL,
            FOREIGN KEY (IdentificadorBomba) REFERENCES Bombas(IdentificadorBomba))
    ''')
            
        self.conn.commit()
        
    @property
    def novo_abastecimento(self):
        return self.__abastecimento
    
    def adicionar_abastecimento(self, IdentificadorBomba, data, litros, valorTotal):
        novo_abastecimento = Abastecimento(IdentificadorBomba, data, litros, valorTotal)
        if not isinstance(novo_abastecimento, Abastecimento):
            raise ValueError("O objeto fornecido não é uma instância da classe Abastecimento.")
        try:
            with self.conn:
                self.cursor.execute("INSERT INTO Abastecimentos (IdentificadorBomba, data, litros, valorTotal) VALUES (?, ?, ?, ?)",
                                    (novo_abastecimento.IdentificadorBomba, novo_abastecimento.data, novo_abastecimento.litros, novo_abastecimento.valorTotal))
                self.conn.commit()
        except sqlite3.IntegrityError as e:
            # Se houver uma violação de integridade (como chave duplicada), lança uma exceção
            if 'FOREIGN KEY constraint failed' in str(e):
                raise ValueError("Erro: Bomba não cadastrada.")
            else:
                raise

    def listar_abastecimentos(self):
        # Listar todos os abastecimentos do banco de dados
        self.cursor.execute("SELECT * FROM Abastecimentos")
        return self.cursor.fetchall()
    
    def buscar_abastecimento(self, identificadorAbastecimento):
        # Buscar um abastecimento específico pelo Identificador
        self.cursor.execute("SELECT * FROM Abastecimentos WHERE IdentificadorAbastecimento = ?", (identificadorAbastecimento,))
        return self.cursor.fetchone()
    
    def remover_abastecimento(self, identificadorAbastecimento):
        # Remover um abastecimento pelo Identificador
        with self.conn:
            self.cursor.execute("DELETE FROM Abastecimentos WHERE IdentificadorAbastecimento = ?", (identificadorAbastecimento,))
            return self.cursor.rowcount > 0
        
    def atualizar_abastecimento(self, identificadorAbastecimento, IdentificadorBomba, data, litros, valorTotal):
        novo_abastecimento = Abastecimento(IdentificadorBomba, data, litros, valorTotal)
        if not isinstance(novo_abastecimento, Abastecimento):
            raise ValueError("O objeto fornecido não é uma instância da classe Abastecimento.")
        try:
            with self.conn:
                self.cursor.execute("UPDATE Abastecimentos SET IdentificadorBomba = ?, data = ?, litros = ?, valorTotal = ? WHERE IdentificadorAbastecimento = ?",
                                    (novo_abastecimento.IdentificadorBomba, novo_abastecimento.data, novo_abastecimento.litros, novo_abastecimento.valorTotal, identificadorAbastecimento))
                self.conn.commit()
        except sqlite3.IntegrityError as e:
            # Se houver uma violação de integridade (como chave duplicada), lança uma exceção
            if 'FOREIGN KEY constraint failed' in str(e):
                raise ValueError("Erro: Bomba não cadastrada.")
            else:
                raise

    @property
    def novo_abastecimento(self):
        return self.__abastecimento
    
    @novo_abastecimento.setter
    def novo_abastecimento(self, value):
        self.__abastecimento = value

    def __del__(self):
        self.conn.close()

        




