class Usuario:
    def __init__(self,cpf: str, email: str, nome: str, telefone: str, senha: str, isGestor: bool):
        self.__cpf = cpf
        self.__email = email
        self.__nome = nome
        self.__telefone = telefone
        self.__senha = senha
        self.__isGestor = isGestor


    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, value):
        self.__cpf = value

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, value):
        self.__telefone = value

    @property
    def login(self):
        return self.__login
    
    @login.setter
    def login(self, value):
        self.__login = value

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, value):
        self.__senha = value

    @property
    def isGestor(self):
        return self.__isGestor
    
    @isGestor.setter
    def isGestor(self, value):
        self.__isGestor = value
        