class Medicao:
    def __init__(self, id=0, id_cliente=0, data=""):
        self.id = id
        self.id_cliente = id_cliente
        self.data = data

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

    def to_dict(self):
        return {
            "id": self.id,
            "id_cliente": self.id_cliente,
            "data": self.data
        }
    

class Medida:
    def __init__(self, id=0, id_medicoes=0, id_partcorpo=0, valor=0.0):
        self.id = id
        self.id_medicoes = id_medicoes
        self.id_partcorpo = id_partcorpo
        self.valor = valor

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

    def to_dict(self):
        return {
            "id": self.id,
            "id_medicoes": self.id_medicoes,
            "id_partcorpo": self.id_partcorpo,
            "valor": self.valor
        }
    
class PartCorpo:
    def __init__(self, id=0, nome="", unidade=""):
        self.id = id
        self.nome = nome
        self.unidade = unidade

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

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "unidade": self.unidade
        }
