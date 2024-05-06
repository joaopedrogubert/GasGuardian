from entidades.tipoCombustivel import TipoCombustivel
from entidades.bombaCombustivel import BombaCombustivel

class Abastecimento:
    def __init__(self, bombaCombustivel: BombaCombustivel, data: str, litros: float, valorTotal: float):
        self.__bombaCombustivel = bombaCombustivel
        self.__data = data
        self.__litros = litros
        self.__valorTotal = valorTotal  

    @property
    def bombaCombustivel(self):
        return self.__bombaCombustivel
    
    @property
    def data(self):
        return self.__data
    
    @property
    def litros(self):
        return self.__litros
    
    @property
    def valorTotal(self):
        return self.__valorTotal
    
    @valorTotal.setter
    def valorTotal(self, value):
        self.__valorTotal = value

    @litros.setter
    def litros(self, value):
        self.__litros = value

    @data.setter
    def data(self, value):
        self.__data = value

    
