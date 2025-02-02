class Plano:
    def __init__(self, id=0, nome="", valor=0.0, tempo=""):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.tempo = tempo

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor
    
    @property
    def tempo(self):
        return self.__tempo
    
    @tempo.setter
    def tempo(self, tempo: str):
        self.__tempo = tempo


