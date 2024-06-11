from entidades.usuario import Usuario
import sqlite3
import hashlib

class ControladorUsuario:
    def __init__(self):
        # Conectar ao banco de dados
        self.conn = sqlite3.connect('/Users/railanabreu/Documents/Projects/GasGuardian/Raillan/dados/DADOS.sqlite')
        self.cursor = self.conn.cursor()
        self.__usuario = Usuario
        self.conn.commit()

    @property
    def nova_usuario(self):
        return self.__usuario
    
    @nova_usuario.setter
    def nova_usuario(self, value):
        if not isinstance(value, Usuario):
            raise ValueError("O objeto fornecido não é uma instância da classe Usuario.")
        self.__usuario = value
        return self.__usuario

    def listar_usuarios(self):
        # Listar todas as usuarios do banco de dados
        self.cursor.execute("SELECT nome, cpf, telefone, email FROM Usuarios")
        return self.cursor.fetchall()
    
    def buscar_usuario(self, cpf):
        # Buscar uma usuario específica pelo CPF
        self.cursor.execute("SELECT * FROM usuarios WHERE cpf = ?", (cpf,))
        return self.cursor.fetchone()
    
    def remover_usuario(self, cpf):
        # Remover uma usuario pelo CPF
        with self.conn:
            self.cursor.execute("DELETE FROM usuarios WHERE cpf = ?", (cpf,))
            return self.cursor.rowcount > 0
        
    def adicionar_usuario(self, cpf, email, nome, telefone, senha, isGestor):
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        if self.validar_dados(cpf, email, nome, telefone, senha):
            try:
                usuario = Usuario(cpf, email, nome, telefone, senha_hash, isGestor)

                if not isinstance(usuario, Usuario):
                    raise ValueError("O objeto fornecido não é uma instância da classe Usuario.")

                with self.conn:
                    self.cursor.execute("INSERT INTO usuarios (cpf, email, nome, telefone, senha, isGestor) VALUES (?, ?, ?, ?, ?, ?)",
                                        (usuario.cpf, usuario.email, usuario.nome, usuario.telefone, usuario.senha, usuario.isGestor))
                    self.conn.commit()
            except sqlite3.IntegrityError as e:
                # Se houver uma violação de integridade (como chave duplicada), lança uma exceção
                if 'UNIQUE constraint failed: usuarios.cpf' in str(e):
                    raise ValueError("Erro: CPF já cadastrado.")
                elif 'UNIQUE constraint failed: usuarios.email' in str(e):
                    raise ValueError("Erro: Email já cadastrado.")
                else:
                    raise
        else:
            raise ValueError("Erro: Dados inválidos.")
    
    def alterar_senha(self, cpf, senha):
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        try:
            with self.conn:
                self.cursor.execute("UPDATE usuarios SET senha = ? WHERE cpf = ?",
                                    (senha_hash, cpf))
                self.conn.commit()
        except sqlite3.IntegrityError as e:
            raise ValueError("Erro ao alterar senha.")
        
    def login_cpf(self, cpf, senha):
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        self.cursor.execute("SELECT * FROM usuarios WHERE cpf = ? AND senha = ?", (cpf, senha_hash))
        return self.cursor.fetchone()
    
    def login_email(self, email, senha):
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        self.cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha_hash))
        return self.cursor.fetchone()
    
    def validar_dados(self, cpf, email, nome, telefone, senha):
        if None in (cpf, email, nome, telefone, senha):
            raise ValueError("Todos os campos são obrigatórios.")

        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError("CPF inválido.")

        if not telefone.isdigit() or len(telefone) < 10 or len(telefone) > 11:
            raise ValueError("Telefone inválido.")

        if not "@" in email or not "." in email:
            raise ValueError("Email inválido.")

        self.cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        if self.cursor.fetchone():
            raise ValueError("Email já cadastrado.")

        # Se não houver nenhum erro encontrado nos dados, retorne True
        return True
    
    def __del__(self):
        self.conn.close()
        

    