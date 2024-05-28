class TipoCombustivel:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, value):
        self.__preco = value

    