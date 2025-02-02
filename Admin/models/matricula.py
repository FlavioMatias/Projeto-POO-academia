from CRUD import CRUD
import json

class Matricula:
    def __init__(self, id=0, id_cliente=0, plano="", data="", validade=""):
        self.id = id
        self.id_cliente = id_cliente
        self.plano = plano
        self.data = data
        self.validade = validade

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def id_cliente(self):
        return self.__id_cliente
    
    @id_cliente.setter
    def id_cliente(self, id_cliente: int):
        self.__id_cliente = id_cliente
    
    @property
    def plano(self):
        return self.__plano
    
    @plano.setter
    def plano(self, plano: str):
        self.__plano = plano
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data: str):
        self.__data = data
    
    @property
    def validade(self):
        return self.__validade
    
    @validade.setter
    def validade(self, validade: str):
        self.__validade = validade

