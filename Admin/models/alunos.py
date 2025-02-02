from CRUD import CRUD
import json

class Aluno:
    def __init__(self, nome : str = None, email : str = None, tel : str = None, data_cadastro : str = None, nascimento : str = None, sexo : str = None, cpf : str = None, rg : str = None, profissao : str = None):
        self.id = 0
        self.nome = nome
        self.email = email
        self.tel = tel
        self.data_cadastro = data_cadastro
        self.nascimento = nascimento
        self.sexo = sexo
        self.cpf = cpf
        self.rg = rg
        self.profissao = profissao

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
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email: str):
        self.__email = email
    
    @property
    def tel(self):
        return self.__tel
    
    @tel.setter
    def tel(self, tel: str):
        self.__tel = tel
    
    @property
    def data_cadastro(self):
        return self.__data_cadastro
    
    @data_cadastro.setter
    def data_cadastro(self, data_cadastro: str):
        self.__data_cadastro = data_cadastro
    
    @property
    def nascimento(self):
        return self.__nascimento
    
    @nascimento.setter
    def nascimento(self, nascimento: str):
        self.__nascimento = nascimento
    
    @property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self, sexo: str):
        self.__sexo = sexo
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf
    
    @property
    def rg(self):
        return self.__rg
    
    @rg.setter
    def rg(self, rg: str):
        self.__rg = rg
    
    @property
    def profissao(self):
        return self.__profissao
    
    @profissao.setter
    def profissao(self, profissao: str):
        self.__profissao = profissao


class Endereco:
    def __init__(self, id=0, id_cliente=0, bairro="", cep="", rua="", numero=""):
        self.__id = id
        self.__id_cliente = id_cliente
        self.__bairro = bairro
        self.__cep = cep
        self.__rua = rua
        self.__numero = numero

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
    def bairro(self):
        return self.__bairro
    
    @bairro.setter
    def bairro(self, bairro: str):
        self.__bairro = bairro
    
    @property
    def cep(self):
        return self.__cep
    
    @cep.setter
    def cep(self, cep: str):
        self.__cep = cep
    
    @property
    def rua(self):
        return self.__rua
    
    @rua.setter
    def rua(self, rua: str):
        self.__rua = rua
    
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero: str):
        self.__numero = numero