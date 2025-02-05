from datetime import datetime

class Medicao:
    def __init__(self, id=0, id_cliente=0, data=""):
        self.id = id
        self.id_cliente = id_cliente
        self.data = data

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def id_cliente(self):
        return self.__id_cliente

    @property
    def data(self):
        return self.__data

    # Setters
    @id.setter
    def id(self, id: int):
        if not isinstance(id, int) or id < 0:
            raise ValueError("O ID deve ser um número inteiro positivo.")
        self.__id = id

    @id_cliente.setter
    def id_cliente(self, id_cliente: int):
        if not isinstance(id_cliente, int) or id_cliente < 0:
            raise ValueError("O ID do cliente deve ser um número inteiro positivo.")
        self.__id_cliente = id_cliente

    @data.setter
    def data(self, data: str):
        try:
            data_obj = datetime.strptime(data, '%d/%m/%Y')
            if data_obj < datetime.today():
                raise ValueError("Data não pode ser no passado.")
            self.__data = data
        except ValueError:
            raise ValueError("Data inválida. Use o formato 'DD/MM/YYYY'.")

    def to_dict(self):
        return {"id": self.id, "id_cliente": self.id_cliente, "data": self.data}

    def __str__(self):
        return f"Medicao(ID: {self.id}, Cliente: {self.id_cliente}, Data: {self.data})"


class Medida:
    def __init__(self, id=0, id_medicoes=0, id_partcorpo=0, valor=0.0):
        self.id = id
        self.id_medicoes = id_medicoes
        self.id_partcorpo = id_partcorpo
        self.valor = valor

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def id_medicoes(self):
        return self.__id_medicoes

    @property
    def id_partcorpo(self):
        return self.__id_partcorpo

    @property
    def valor(self):
        return self.__valor

    # Setters
    @id.setter
    def id(self, id: int):
        if not isinstance(id, int) or id < 0:
            raise ValueError("O ID deve ser um número inteiro positivo.")
        self.__id = id

    @id_medicoes.setter
    def id_medicoes(self, id_medicoes: int):
        if not isinstance(id_medicoes, int) or id_medicoes < 0:
            raise ValueError("O ID da medição deve ser um número inteiro positivo.")
        self.__id_medicoes = id_medicoes

    @id_partcorpo.setter
    def id_partcorpo(self, id_partcorpo: int):
        if not isinstance(id_partcorpo, int) or id_partcorpo < 0:
            raise ValueError("O ID da parte do corpo deve ser um número inteiro positivo.")
        self.__id_partcorpo = id_partcorpo

    @valor.setter
    def valor(self, valor: float):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("O valor deve ser um número positivo.")
        self.__valor = float(valor)

    def to_dict(self):
        return {
            "id": self.id,
            "id_medicoes": self.id_medicoes,
            "id_partcorpo": self.id_partcorpo,
            "valor": self.valor
        }

    def __str__(self):
        return f"Medida(ID: {self.id}, Medição: {self.id_medicoes}, Parte do Corpo: {self.id_partcorpo}, Valor: {self.valor})"


class PartCorpo:
    def __init__(self, id=0, nome="", unidade=""):
        self.id = id
        self.nome = nome
        self.unidade = unidade

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def unidade(self):
        return self.__unidade

    # Setters
    @id.setter
    def id(self, id: int):
        if not isinstance(id, int) or id < 0:
            raise ValueError("O ID deve ser um número inteiro positivo.")
        self.__id = id

    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome deve ser uma string não vazia.")
        self.__nome = nome

    @unidade.setter
    def unidade(self, unidade: str):
        unidades_validas = ["cm", "m", "kg", "mmHg", "bpm", "%"]
        if not isinstance(unidade, str) or not unidade.strip():
            raise ValueError("A unidade deve ser uma string não vazia.")
        
        elif not unidade.lower() in unidades_validas:
            raise ValueError("unidade não reconhecida")
        
        else:
            self.__unidade = unidade

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "unidade": self.unidade}

    def __str__(self):
        return f"PartCorpo(ID: {self.id}, Nome: {self.nome}, Unidade: {self.unidade})"
