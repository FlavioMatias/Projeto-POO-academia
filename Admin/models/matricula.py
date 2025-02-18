from datetime import datetime

class Matricula:
    def __init__(self, id, id_aluno, plano, data, validade, ativa=True):
        self.id = id
        self.id_aluno = id_aluno
        self.plano = plano
        self.data = data
        self.validade = validade
        self.ativa = ativa

    def to_dict(self):
        return {
            "id": self.id,
            "id_aluno": self.id_aluno,
            "plano": self.plano,
            "data": self.data,
            "validade": self.validade,
            "ativa": self.ativa
        }
    
    def __str__(self):
        return (f"Matricula: \n"
                f"  id={self.id},\n"
                f"  id_aluno={self.id_aluno},\n"
                f"  plano={self.plano},\n"
                f"  data={self.data},\n"
                f"  validade={self.validade}\n")
    
    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def id_aluno(self):
        return self.__id_aluno

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

    @id_aluno.setter
    def id_aluno(self, id_aluno: int):
        if not isinstance(id_aluno, int):
            raise TypeError("O id_aluno deve ser um número inteiro!")
        if id_aluno < 0:
            raise ValueError("O id_aluno não pode ser negativo!")
        self.__id_aluno = id_aluno

    @plano.setter
    def plano(self, plano: int):
        if not isinstance(plano, int):
            raise TypeError("Plano inválido")
        self.__plano = plano

    @data.setter
    def data_cadastro(self, data: str):
        try:
            data_obj = datetime.strptime(data, '%d/%m/%Y')
        except ValueError:
            raise ValueError("Data  inválida. Use o formato 'DD/MM/YYYY'.")
        
        if data_obj > datetime.today():
            raise ValueError("Data não pode ser no futuro.")

        self.__data = data

    @validade.setter
    def validade(self, validade: str):
        try:
            data_obj = datetime.strptime(validade, '%d/%m/%Y')
        except ValueError:
            raise ValueError("Data  inválida. Use o formato 'DD/MM/YYYY'.")
        
        if data_obj < datetime.today():
            raise ValueError("Data não pode ser no passado.")
        
        self.__validade = validade

