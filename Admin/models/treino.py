from datetime import datetime

class TreinoAluno:
    def __init__(self, id=0, id_aluno=0, data="", atv=True):
        self.id = id
        self.id_aluno = id_aluno
        self.data = data
        self.ativo = atv

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def id_aluno(self):
        return self.__id_aluno

    @property
    def data(self):
        return self.__data
    
    @property
    def ativo(self):
        return self.__ativo

    # Setters
    @id.setter
    def id(self, id: int):
        if not isinstance(id, int) or id < 0:
            raise ValueError("O ID deve ser um número inteiro positivo.")
        self.__id = id

    @id_aluno.setter
    def id_aluno(self, id_aluno: int):
        if not isinstance(id_aluno, int) or id_aluno < 0:
            raise ValueError("O ID do aluno deve ser um número inteiro positivo.")
        self.__id_aluno = id_aluno

    @data.setter
    def data(self, data: str):
        try:
            variavel = datetime.strptime(data, "%d/%m/%Y").date()
            self.__data = data
        except ValueError:
            raise ValueError("A data deve estar no formato 'DD/MM/YYYY'.")

    @ativo.setter
    def ativo(self, ativo: bool):
        self.__ativo = ativo

    def to_dict(self):
        return {
            "id": self.id,
            "id_aluno": self.id_aluno,
            "data": self.data,
            "ativo": self.ativo
        }

    def __str__(self):
        return f"TreinoAluno(ID: {self.id}, Aluno: {self.id_aluno}, Data: {self.data}, Ativo: {self.ativo})"


class Treino:
    def __init__(self, id=0, id_musculo=0, id_treino=0, descricao=""):
        self.id = id
        self.id_musculo = id_musculo
        self.id_treino = id_treino
        self.descricao = descricao

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def id_musculo(self):
        return self.__id_musculo

    @property
    def id_treino(self):
        return self.__id_treino

    @property
    def descricao(self):
        return self.__descricao

    # Setters
    @id.setter
    def id(self, id: int):
        if not isinstance(id, int) or id < 0:
            raise ValueError("O ID deve ser um número inteiro positivo.")
        self.__id = id

    @id_musculo.setter
    def id_musculo(self, id_musculo: int):
        if not isinstance(id_musculo, int) or id_musculo < 0:
            raise ValueError("O ID do músculo deve ser um número inteiro positivo.")
        self.__id_musculo = id_musculo

    @id_treino.setter
    def id_treino(self, id_treino: int):
        if not isinstance(id_treino, int) or id_treino < 0:
            raise ValueError("O ID do treino deve ser um número inteiro positivo.")
        self.__id_treino = id_treino

    @descricao.setter
    def descricao(self, descricao: str):
        if not isinstance(descricao, str) or not descricao.strip():
            raise ValueError("A descrição não pode estar vazia.")
        self.__descricao = descricao.strip()

    def to_dict(self):
        return {
            "id": self.id,
            "id_musculo": self.id_musculo,
            "id_treino": self.id_treino,
            "descricao": self.descricao
        }

    def __str__(self):
        return f"Treino(ID: {self.id}, Músculo: {self.id_musculo}, Treino: {self.id_treino}, Descrição: {self.descricao})"


class Musculo:
    def __init__(self, id=0, nome=""):
        self.id = id
        self.nome = nome

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    # Setters
    @id.setter
    def id(self, id: int):
        if not isinstance(id, int) or id < 0:
            raise ValueError("O ID do músculo deve ser um número inteiro positivo.")
        self.__id = id

    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome do músculo não pode estar vazio.")
        self.__nome = nome.strip()

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome
        }

    def __str__(self):
        return f"Musculo(ID: {self.id}, Nome: {self.nome})"
