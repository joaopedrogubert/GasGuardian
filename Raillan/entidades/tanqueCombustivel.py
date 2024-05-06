from entidades.tipoCombustivel import TipoCombustivel

class TanqueCombustivel:
    def __init__(self,capacidadeMaxima, porcentagemAlerta,tipoCombustivel,columeAtual):
        self.__capacidadeMaxima = capacidadeMaxima
        self.__porcentagemAlerta = porcentagemAlerta
        self.__tipoCombustivel = TipoCombustivel #subistituir quando o paixao subir a branch para o objeto tipo de combustivel.
        self.__volumeAtual = columeAtual

    @property
    def capacidadeMaxima(self):
        return self.__capacidadeMaxima

    @capacidadeMaxima.setter
    def capacidadeMaxima(self, value):
        self.__capacidadeMaxima = value

    @property
    def porcentagemAlerta(self):
        return self.__porcentagemAlerta

    @porcentagemAlerta.setter
    def porcentagemAlerta(self, value):
        self.__porcentagemAlerta = value

    @property
    def tipoCombustivel(self):
        return self.__tipoCombustivel

    @tipoCombustivel.setter
    def tipoCombustivel(self, value):
        self.__tipoCombustivel = value

    @property
    def volumeAtual(self):
        return self.__volumeAtual

    @volumeAtual.setter
    def volumeAtual(self, value):
        self.__volumeAtual = value
