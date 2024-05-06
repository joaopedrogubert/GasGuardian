from entidades.tipoCombustivel import TipoCombustivel

class BombaCombustivel:
    def __init__(self, autoAbastecimento: bool, tipoCombustivel: list , bombaAtiva: bool):
        self.__autoAbastecimento = autoAbastecimento
        self.__tipoCombustivel = [TipoCombustivel]
        self.__bombaAtiva = bombaAtiva

    @property
    def autoAbastecimento(self):
        return self.__autoAbastecimento
    
    @autoAbastecimento.setter
    def autoAbastecimento(self, value):
        self.__autoAbastecimento = value

    @property
    def tipoCombustivel(self):
        return self.__tipoCombustivel
    
    @tipoCombustivel.setter
    def tipoCombustivel(self, value):
        self.__tipoCombustivel = value
    
    @property
    def bombaAtiva(self):
        return self.__bombaAtiva
    
    @bombaAtiva.setter
    def bombaAtiva(self, value):
        self.__bombaAtiva = value