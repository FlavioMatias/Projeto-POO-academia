import re

class Plano:
    TEMPO_REGEX = re.compile(r"^\d+\s(ano|anos|mes|meses|semana|semanas)$")

    def __init__(self, id=0, nome="", valor=0.0, tempo=""):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.tempo = tempo

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor

    @property
    def tempo(self):
        return self.__tempo

    # Setters
    @id.setter
    def id(self, id: int):
        if not isinstance(id, int) or id < 0:
            raise ValueError("O ID deve ser um número inteiro positivo.")
        self.__id = id

    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome do plano não pode estar vazio.")
        self.__nome = nome.strip()

    @valor.setter
    def valor(self, valor: float):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("O valor deve ser um número positivo.")
        self.__valor = float(valor)

    @tempo.setter
    def tempo(self, tempo: str):
        tempo = tempo.lower().replace("mês", "mes")  
        if not self.TEMPO_REGEX.match(tempo):
            raise ValueError('O tempo deve estar no formato "<número> <unidade>", exemplo: "1 ano", "12 meses", "2 semanas".')
        self.__tempo = tempo

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "valor": self.valor,
            "tempo": self.tempo
        }

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Valor: R$ {self.valor:.2f}, Tempo: {self.tempo})"
