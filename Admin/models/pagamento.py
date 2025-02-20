from datetime import datetime

class Pagamento:
    def __init__(self, id=0, id_matricula=0, id_cliente=0, emissao="", vencimento="", data_pagamento=None, valor=0.0, pago=False):
        self.id = id
        self.id_matricula = id_matricula
        self.id_cliente = id_cliente
        self.emissao = emissao
        self.vencimento = vencimento
        self.data_pagamento = data_pagamento
        self.valor = valor
        self.pago = pago

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def id_matricula(self):
        return self.__id_matricula

    @property
    def id_cliente(self):
        return self.__id_cliente

    @property
    def emissao(self):
        return self.__emissao

    @property
    def vencimento(self):
        return self.__vencimento

    @property
    def data_pagamento(self):
        return self.__data_pagamento

    @property
    def valor(self):
        return self.__valor

    @property
    def pago(self):
        return self.__pago

    # Setters
    @id.setter
    def id(self, id: int):
        if not isinstance(id, int) or id < 0:
            raise ValueError("O ID deve ser um número inteiro positivo.")
        self.__id = id

    @id_matricula.setter
    def id_matricula(self, id_matricula: int):
        if not isinstance(id_matricula, int) or id_matricula < 0:
            raise ValueError("O ID da matrícula deve ser um número inteiro positivo.")
        self.__id_matricula = id_matricula

    @id_cliente.setter
    def id_cliente(self, id_cliente: int):
        if not isinstance(id_cliente, int) or id_cliente < 0:
            raise ValueError("O ID do cliente deve ser um número inteiro positivo.")
        self.__id_cliente = id_cliente

    @emissao.setter
    def emissao(self, emissao: str):
        self.__emissao = self.validar_data(emissao, "emissao")

    @vencimento.setter
    def vencimento(self, vencimento: str):
        vencimento_date = self.validar_data(vencimento, "vencimento")
        if hasattr(self, "_Pagamento__emissao") and vencimento_date < self.__emissao:
            raise ValueError("A data de vencimento não pode ser anterior à data de emissão.")
        self.__vencimento = vencimento_date

    @data_pagamento.setter
    def data_pagamento(self, data_pagamento):
        if data_pagamento is None or data_pagamento == "":
            self.__data_pagamento = None
        else:
            pagamento_date = self.validar_data(data_pagamento, "data_pagamento")
            if pagamento_date < self.__emissao:
                raise ValueError("A data de pagamento não pode ser anterior à data de emissão.")
            self.__data_pagamento = pagamento_date

    @valor.setter
    def valor(self, valor: float):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("O valor deve ser um número positivo.")
        self.__valor = float(valor)

    @pago.setter
    def pago(self, pago: bool):
        if not isinstance(pago, bool):
            raise ValueError("O campo 'pago' deve ser um valor booleano (True ou False).")
        self.__pago = pago

    def validar_data(self, data_str, campo):
        """ Valida se a data está no formato dd/mm/aaaa e a converte para datetime.date """
        if not isinstance(data_str, str):  # Garante que o valor seja uma string
            raise ValueError(f"A data de {campo} deve ser uma string no formato DD/MM/YYYY.")
        
        try:
            # Tenta converter a string para datetime.date
            return datetime.strptime(data_str, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError(f"A data de {campo} deve estar no formato DD/MM/YYYY.")

    def to_dict(self):
        return {
            "id": self.id,
            "id_matricula": self.id_matricula,
            "id_cliente": self.id_cliente,
            "emissao": self.emissao.strftime("%d/%m/%Y"),
            "vencimento": self.vencimento.strftime("%d/%m/%Y"),
            "data_pagamento": self.data_pagamento.strftime("%d/%m/%Y") if self.data_pagamento else None,
            "valor": self.valor,
            "pago": self.pago
        }

    def __str__(self):
        return f"Pagamento(ID: {self.id}, Matrícula: {self.id_matricula}, Cliente: {self.id_cliente}, Emissão: {self.emissao}, Vencimento: {self.vencimento}, Data Pagamento: {self.data_pagamento}, Valor: R$ {self.valor:.2f}, Pago: {self.pago})"