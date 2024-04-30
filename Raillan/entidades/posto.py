class PostoGasolina:
    def __init__(self, cnpj, chavePix, nomePosto):
        self.__cnpj = cnpj
        self.__chavePix = chavePix  
        self.__nomePosto = nomePosto

    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def chavePix(self):
        return self.__chavePix

    @chavePix.setter
    def chavePix(self, chavePix):
        self.__chavePix = chavePix

    @property
    def nomePosto(self):
        return self.__nomePosto

    @nomePosto.setter
    def nomeposto(self, nomePosto):
        self.__nomePosto = nomePosto