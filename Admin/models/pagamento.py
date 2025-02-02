class Pagamento:
    def __init__(self, id=0, id_matricula=0, id_cliente=0, emissao="", vencimento="", data_pagamento="", valor=0.0, pago=False):
        self.id = id
        self.id_matricula = id_matricula
        self.id_cliente = id_cliente
        self.emissao = emissao
        self.vencimento = vencimento
        self.data_pagamento = data_pagamento
        self.valor = valor
        self.pago = pago

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def id_matricula(self):
        return self.__id_matricula
    
    @id_matricula.setter
    def id_matricula(self, id_matricula: int):
        self.__id_matricula = id_matricula

    @property
    def id_cliente(self):
        return self.__id_cliente
    
    @id_cliente.setter
    def id_cliente(self, id_cliente: int):
        self.__id_cliente = id_cliente

    @property
    def emissao(self):
        return self.__emissao
    
    @emissao.setter
    def emissao(self, emissao: str):
        self.__emissao = emissao

    @property
    def vencimento(self):
        return self.__vencimento
    
    @vencimento.setter
    def vencimento(self, vencimento: str):
        self.__vencimento = vencimento

    @property
    def data_pagamento(self):
        return self.__data_pagamento
    
    @data_pagamento.setter
    def data_pagamento(self, data_pagamento: str):
        self.__data_pagamento = data_pagamento

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor

    @property
    def pago(self):
        return self.__pago
    
    @pago.setter
    def pago(self, pago: bool):
        self.__pago = pago
