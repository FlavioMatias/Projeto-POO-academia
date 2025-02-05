from datetime import datetime

class Matricula:
    def __init__(self, id, id_cliente, plano, data, validade):
        self.id = id
        self.id_cliente = id_cliente
        self.plano = plano
        self.data = data
        self.validade = validade

    def to_dict(self):
        return {
            "id": self.id,
            "id_cliente": self.id_cliente,
            "plano": self.plano,
            "data": self.data,
            "validade": self.validade
        }
    
    def __str__(self):
        return (f"Matricula: \n"
                f"  id={self.id},\n"
                f"  id_cliente={self.id_cliente},\n"
                f"  plano={self.plano},\n"
                f"  data={self.data},\n"
                f"  validade={self.validade}\n")
    
    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def id_cliente(self):
        return self.__id_cliente

    @property
    def plano(self):
        return self.__plano

    @property
    def data(self):
        return self.__data

    @property
    def validade(self):
        return self.__validade

    # Setters
    @id.setter
    def id(self, id: int):
        if not isinstance(id, int):
            raise TypeError("O id deve ser um número inteiro!")
        if id < 0:
            raise ValueError("O id não pode ser negativo!")
        self.__id = id

    @id_cliente.setter
    def id_cliente(self, id_cliente: int):
        if not isinstance(id_cliente, int):
            raise TypeError("O id_cliente deve ser um número inteiro!")
        if id_cliente < 0:
            raise ValueError("O id_cliente não pode ser negativo!")
        self.__id_cliente = id_cliente

    @plano.setter
    def plano(self, plano: int):
        if not isinstance(plano, int):
            raise TypeError("Plano inválido")
        self.__plano = plano

    @data.setter
    def data(self, data: str):
        try:
            datetime.strptime(data, '%d/%m/%Y')
            self.__data = data
        except ValueError:
            raise ValueError("Data de cadastro inválida. Use o formato 'DD/MM/YYYY'.")

    @validade.setter
    def validade(self, validade: str):
        if not isinstance(validade, str):
            raise TypeError("A validade deve ser uma string!")
        self.__validade = validade

