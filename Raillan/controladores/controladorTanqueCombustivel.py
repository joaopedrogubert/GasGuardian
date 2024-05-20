import sqlite3
from entidades.tanqueCombustivel import TanqueCombustivel

class ControladorTanqueCombustivel:
    def __init__(self):
        self.conn = sqlite3.connect('/Users/railanabreu/Documents/Projects/gas-guardian/Raillan/dados/dadosTanqueCombustivel.sqlite')
        self.cursor = self.conn.cursor()
        self.__tanque = TanqueCombustivel
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tanques (
            IdentificadorTanque INTEGER PRIMARY KEY AUTOINCREMENT,
            capacidadeMaxima NUMERIC  NOT NULL,
            porcentagemAlerta NUMERIC NOT NULL,
            tipoCombustivel TEXT NOT NULL,
            volumeAtual NUMERIC NOT NULL)
    ''')
        
        self.conn.commit()

    @property
    def novo_tanque(self):
        return self.__tanque
    
    def adicionar_tanque(self, capacidadeMaxima, porcentagemAlerta, tipoCombustivel, volumeAtual):

        novo_tanque = TanqueCombustivel(capacidadeMaxima, porcentagemAlerta, tipoCombustivel, volumeAtual)

        if not isinstance(novo_tanque, TanqueCombustivel):
            raise ValueError("O objeto fornecido não é uma instância da classe TanqueCombustivel.")

        try:
            with self.conn:
                self.cursor.execute("INSERT INTO Tanques (capacidadeMaxima, porcentagemAlerta, tipoCombustivel, volumeAtual) VALUES (?, ?, ?, ?)",
                                    (novo_tanque.capacidadeMaxima, novo_tanque.porcentagemAlerta, novo_tanque.tipoCombustivel, novo_tanque.volumeAtual))
                self.conn.commit()
        except sqlite3.IntegrityError as e:
            # Se houver uma violação de integridade (como chave duplicada), lança uma exceção
            if 'UNIQUE constraint failed: Tanques.capacidadeMaxima' in str(e):
                raise ValueError("Erro: Capacidade Máxima já cadastrada.")
            elif 'UNIQUE constraint failed: Tanques.porcentagemAlerta' in str(e):
                raise ValueError("Erro: Porcentagem de Alerta já cadastrada.")
            else:
                raise

    def listar_tanques(self):
        # Executar a consulta SQL para obter todos os tanques
        self.cursor.execute("SELECT * FROM Tanques")
        
        # Obter os cabeçalhos das colunas
        cabecalhos = [description[0] for description in self.cursor.description]
        
        # Obter todos os dados
        tanques = self.cursor.fetchall()

        return cabecalhos, tanques
    
    def buscar_tanque(self, identificadorTanque):
        # Buscar um tanque específico pelo Identificador
        self.cursor.execute("SELECT * FROM Tanques WHERE IdentificadorTanque = ?", (identificadorTanque,))
        return self.cursor.fetchone()
    
    def remover_tanque(self, identificadorTanque):
        # Remover um tanque pelo Identificador
        with self.conn:
            self.cursor.execute("DELETE FROM Tanques WHERE IdentificadorTanque = ?", (identificadorTanque,))
            return self.cursor.rowcount > 0
        
    def atualizar_tanque(self, tanque):
        if not isinstance(tanque, TanqueCombustivel):
            raise ValueError("O objeto fornecido não é uma instância da classe TanqueCombustivel.")
        try:
            with self.conn:
                update_query = "UPDATE Tanques SET"
                update_values = []
            if tanque.capacidadeMaxima is not None:
                update_query += " capacidadeMaxima = ?,"
                update_values.append(tanque.capacidadeMaxima)
            if tanque.porcentagemAlerta is not None:
                update_query += " porcentagemAlerta = ?,"
                update_values.append(tanque.porcentagemAlerta)
            if tanque.tipoCombustivel is not None:
                update_query += " tipoCombustivel = ?,"
                update_values.append(tanque.tipoCombustivel)
            if tanque.volumeAtual is not None:
                update_query += " volumeAtual = ?,"
                update_values.append(tanque.volumeAtual)
            update_query = update_query.rstrip(",") + " WHERE IdentificadorTanque = ?"
            update_values.append(tanque.IdentificadorTanque)
            self.cursor.execute(update_query, update_values)
            self.conn.commit()
            if self.cursor.rowcount > 0:
                print("Tanque atualizado com sucesso!")
                return True
            else:
                print("Nenhum tanque encontrado com o identificador fornecido.")
                return False
        except sqlite3.Error as e:
            print(f"Erro ao atualizar o tanque: {e}")
            return False

            

    def __del__(self):
        self.conn.close()
