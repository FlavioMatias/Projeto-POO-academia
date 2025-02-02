class Medicao:
    def __init__(self, id=0, id_cliente=0, data=""):
        self.__id = id
        self.__id_cliente = id_cliente
        self.__data = data

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
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data: str):
        self.__data = data

class Medida:
    def __init__(self, id=0, id_medicoes=0, id_partcorpo=0, valor=0.0):
        self.__id = id
        self.__id_medicoes = id_medicoes
        self.__id_partcorpo = id_partcorpo
        self.__valor = valor

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def id_medicoes(self):
        return self.__id_medicoes
    
    @id_medicoes.setter
    def id_medicoes(self, id_medicoes: int):
        self.__id_medicoes = id_medicoes

    @property
    def id_partcorpo(self):
        return self.__id_partcorpo
    
    @id_partcorpo.setter
    def id_partcorpo(self, id_partcorpo: int):
        self.__id_partcorpo = id_partcorpo

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor

class PartCorpo:
    def __init__(self, id=0, nome="", unidade=""):
        self.__id = id
        self.__nome = nome
        self.__unidade = unidade

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
    def unidade(self):
        return self.__unidade
    
    @unidade.setter
    def unidade(self, unidade: str):
        self.__unidade = unidade

