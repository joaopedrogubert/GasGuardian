from ..controladores.controladorPosto import ControladorPosto
from ..controladores.controladorTanqueCombustivel import ControladorTanqueCombustivel
from ..controladores.controladorAbastecimento import ControladorAbastecimento
from ..controladores.controladorBombaCombustivel import ControladorBombaCombustivel
from ..controladores.controladorTipoCombustivel import ControladorTipoCombustivel


class ControladorSistema:
    def __init__(self) -> None:
        self.__controladorPosto = ControladorPosto(self)
        self.__controladorTanqueCombustivel = ControladorTanqueCombustivel(self)
        self.__controladorAbastecimento = ControladorAbastecimento(self)
        self.__controladorBombaCombustivel = ControladorBombaCombustivel(self)
        self.__controladorTipoCombustivel = ControladorTipoCombustivel(self)

    @property
    def controladorPosto(self):
        return self.__controladorPosto
    
    @property
    def controladorTanqueCombustivel(self):
        return self.__controladorTanqueCombustivel
    
    @property
    def controladorAbastecimento(self):
        return self.__controladorAbastecimento
    
    @property
    def controladorBombaCombustivel(self):
        return self.__controladorBombaCombustivel

    @property
    def controladorTipoCombustivel(self):
        return self.__controladorTipoCombustivel
