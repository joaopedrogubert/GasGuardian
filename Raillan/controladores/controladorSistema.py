from controladores.controladorPosto import ControladorPosto
from controladores.controladorTanqueCombustivel import ControladorTanqueCombustivel
from controladores.controladorAbastecimento import ControladorAbastecimento
from controladores.controladorBombaCombustivel import ControladorBombaCombustivel
from controladores.controladorTipoCombustivel import ControladorTipoCombustivel
from telas.telaSitemaPrincipal import MenuPrincipal



class ControladorSistema:
    def __init__(self) -> None:
        self.__TelaPrincipal = MenuPrincipal()
        self.__controladorPosto = ControladorPosto()
        self.__controladorTanqueCombustivel = ControladorTanqueCombustivel()
        self.__controladorAbastecimento = ControladorAbastecimento()
        self.__controladorBombaCombustivel = ControladorBombaCombustivel()
        self.__controladorTipoCombustivel = ControladorTipoCombustivel()

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
    @property
    def TelaPrincipal(self):
        return self.__TelaPrincipal
    
    def abre_tela_principal(self):
        self.__TelaPrincipal.mainloop()