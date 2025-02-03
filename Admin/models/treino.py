class TreinoAluno:
    def __init__(self, id=0, id_aluno=0, data="", data_final=""):
        self.__id = id
        self.__id_aluno = id_aluno
        self.__data = data
        self.__data_final = data_final

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def id_aluno(self):
        return self.__id_aluno
    
    @id_aluno.setter
    def id_aluno(self, id_aluno: int):
        self.__id_aluno = id_aluno

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def data_final(self):
        return self.__data_final
    
    @data_final.setter
    def data_final(self, data_final: str):
        self.__data_final = data_final

    def to_dict(self):
        return {
            "id": self.__id,
            "id_aluno": self.__id_aluno,
            "data": self.__data,
            "data_final": self.__data_final
        }
    
class Treino:
    def __init__(self, id=0, id_musculo=0, id_treino=0, descricao=""):
        self.__id = id
        self.__id_musculo = id_musculo
        self.__id_treino = id_treino
        self.__descricao = descricao

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def id_musculo(self):
        return self.__id_musculo

    @id_musculo.setter
    def id_musculo(self, id_musculo: int):
        self.__id_musculo = id_musculo

    @property
    def id_treino(self):
        return self.__id_treino

    @id_treino.setter
    def id_treino(self, id_treino: int):
        self.__id_treino = id_treino

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    def to_dict(self):
        return {
            "id": self.__id,
            "id_musculo": self.__id_musculo,
            "id_treino": self.__id_treino,
            "descricao": self.__descricao
        }

class Musculo:
    def __init__(self, id=0, nome=""):
        self.__id = id
        self.__nome = nome

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

    def to_dict(self):
        return {
            "id": self.__id,
            "nome": self.__nome
        }