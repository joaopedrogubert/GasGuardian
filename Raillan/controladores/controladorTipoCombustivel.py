import sqlite3
from entidades.tipoCombustivel import TipoCombustivel

class ControladorTipoCombustivel:
    def __init__(self):
        self.conn = sqlite3.connect('/Users/railanabreu/Documents/Projects/GasGuardian/Raillan/dados/DADOS.sqlite')
        self.cursor = self.conn.cursor()
        self.__tipoCombustivel = TipoCombustivel


    def adicionar_tipo_combustivel(self, id: int, nome: str, preco: float):
        tipoCombustivel = TipoCombustivel(id, nome, preco)
        if not isinstance(tipoCombustivel, TipoCombustivel):
            raise ValueError("O objeto fornecido não é uma instância da classe TipoCombustivel.")
        try:
            with self.conn:
                self.cursor.execute("INSERT INTO TipoCombustivel (IdentificadorTipoCombustivel, nome, preco) VALUES (?, ?, ?)",
                                    (tipoCombustivel.id, tipoCombustivel.nome, tipoCombustivel.preco))
                self.conn.commit()

        except sqlite3.IntegrityError as e:
            # Se houver uma violação de integridade (como chave duplicada), lança uma exceção
            if 'UNIQUE constraint failed: TipoCombustivel.IdentificadorTipoCombustivel' in str(e):
                raise ValueError("Erro: Identificador já cadastrado.")
            elif 'UNIQUE constraint failed: TipoCombustivel.nome' in str(e):
                raise ValueError("Erro: Nome já cadastrado.")
            else:
                raise
    
    def listar_tipo_combustivel(self):
        self.cursor.execute("SELECT * FROM TipoCombustivel")
        return self.cursor.fetchall()
    
    def buscar_tipo_combustivel(self, id: int):
        self.cursor.execute("SELECT * FROM TipoCombustivel WHERE IdentificadorTipoCombustivel = ?", (id,))
        return self.cursor.fetchone()

    
    def remover_tipo_combustivel(self, id: int):
        with self.conn:
            self.cursor.execute("DELETE FROM TipoCombustivel WHERE IdentificadorTipoCombustivel = ?", (id,))
            return self.cursor.rowcount > 0
        
    
    def atualizar_tipo_combustivel(self, id: int, nome: str, preco: float):
        tipoCombustivel = TipoCombustivel(id, nome, preco)
        if not isinstance(tipoCombustivel, TipoCombustivel):
            raise ValueError("O objeto fornecido não é uma instância da classe TipoCombustivel.")
        try:
            with self.conn:
                self.cursor.execute("UPDATE TipoCombustivel SET nome = ?, preco = ? WHERE IdentificadorTipoCombustivel = ?",
                                    (tipoCombustivel.nome, tipoCombustivel.preco, tipoCombustivel.id))
                self.conn.commit()
        except sqlite3.IntegrityError as e:
            # Se houver uma violação de integridade (como chave duplicada), lança uma exceção
            if 'UNIQUE constraint failed: TipoCombustivel.IdentificadorTipoCombustivel' in str(e):
                raise ValueError("Erro: Identificador já cadastrado.")
            elif 'UNIQUE constraint failed: TipoCombustivel.nome' in str(e):
                raise ValueError("Erro: Nome já cadastrado.")
            else:
                raise

    @property
    def novo_tipo_combustivel(self):
        return self.__tipoCombustivel
    
    @novo_tipo_combustivel.setter
    def novo_tipo_combustivel(self, value):
        self.__tipoCombustivel = value

    def __del__(self):
        self.conn.close()
    

