import json
import re
from datetime import datetime

class Aluno:
    def __init__(self,id = 0, nome : str = None, email : str = None, tel : str = None, data_cadastro : str = None, nascimento : str = None, sexo : str = None, cpf : str = None, rg : str = None, profissao : str = None):
        self.id = id
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
        if not isinstance(id, int):
            raise ValueError("ID do aluno invalido")
        self.__id = id

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome : str):
        if not isinstance(nome, str):
            raise ValueError("Nome deve ser uma string.")
        if len(nome) < 2:
            raise ValueError("Nome deve ter pelo menos 2 caracteres.")
        if not nome.isalpha() and not nome.replace(" ", "").isalpha():
            raise ValueError("Nome deve conter apenas letras e espaços.")
        if not nome.istitle():
            raise ValueError("Nome deve começar com letra maiúscula.")
        
        self.__nome = nome
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email: str):
        if not isinstance(email, str):
            raise ValueError("E-mail deve ser uma string.")
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(regex, email):
            raise ValueError("E-mail inválido. O formato correto é 'exemplo@dominio.com'.")
        
        self.__email = email
    
    @property
    def tel(self):
        return self.__tel
    
    @tel.setter
    def tel(self, tel: str):
        if not isinstance(tel, str):
            raise ValueError("Telefone deve ser uma string.")

        regex = r'^\(?\d{2}\)?\s?\d{4,5}-\d{4}$'
        if not re.match(regex, tel):
            raise ValueError("Telefone inválido. O formato correto é (XX) XXXXX-XXXX ou (XX) XXXX-XXXX.")
        self.__tel = tel
    
    @property
    def data_cadastro(self):
        return self.__data_cadastro
    
    @data_cadastro.setter
    def data_cadastro(self, data_cadastro: str):
        try:
            data_obj = datetime.strptime(data_cadastro, '%d/%m/%Y')
            self.__data_cadastro = data_cadastro
        except ValueError:
            raise ValueError("Data de cadastro inválida. Use o formato 'DD/MM/YYYY'.")
        
    @property
    def nascimento(self):
        return self.__nascimento
    
    @nascimento.setter
    def nascimento(self, nascimento: str):
        try:
            data_obj = datetime.strptime(nascimento, '%d/%m/%Y')
            self.__nascimento = nascimento
        except ValueError:
            raise ValueError("Data de nascimento inválida. Use o formato 'DD/MM/YYYY'.")
        self.__nascimento = nascimento
    
    @property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self, sexo: str):
        sexo = sexo.upper()
        
        if sexo in ['M', 'F', 'MASCULINO', 'FEMININO', 'OUTRO']:
            self.__sexo = sexo
        else:
            raise ValueError("Sexo inválido.")
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf: str):
        cpf = re.sub(r'\D', '', cpf)

        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("CPF deve conter 11 dígitos numéricos.")
        
        if not self.__validar_cpf(cpf):
            raise ValueError("CPF inválido.")
        
        self.__cpf = cpf
    
    @property
    def rg(self):
        return self.__rg
    
    @rg.setter
    def rg(self, rg: str):
        rg = re.sub(r'\D', '', rg)

        if len(rg) != 9 or not rg.isdigit():
            raise ValueError("RG deve conter 9 dígitos numéricos.")
        self.__rg = rg
    
    @property
    def profissao(self):
        return self.__profissao
    
    @profissao.setter
    def profissao(self, profissao: str):
        if len(profissao) >=2 and isinstance(profissao, str):
            self.__profissao = profissao
        else:
            raise ValueError('profissão invalida')


    def __validar_cpf(self, cpf: str) -> bool:
        def calcular_digito(cpf: str, peso: list) -> int:
            soma = sum(int(cpf[i]) * peso[i] for i in range(len(peso)))
            resto = soma % 11
            return 0 if resto < 2 else 11 - resto

        peso1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        digito1 = calcular_digito(cpf, peso1)

        peso2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        digito2 = calcular_digito(cpf, peso2)

        return cpf[-2:] == f"{digito1}{digito2}"
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'tel': self.tel,
            'data_cadastro': self.data_cadastro,
            'nascimento': self.nascimento,
            'sexo': self.sexo,
            'cpf': self.cpf,
            'rg': self.rg,
            'profissao': self.profissao
        }


class Endereco:
    def __init__(self, id=0, id_cliente=0, bairro="", cep="", rua="", numero=""):
        self.id = id
        self.id_cliente = id_cliente
        self.bairro = bairro
        self.cep = cep
        self.rua = rua
        self.numero = numero

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id: int):
        if not isinstance(id, int) or id < 0:
            raise ValueError("ID deve ser um número inteiro não negativo.")
        self.__id = id
    
    @property
    def id_cliente(self):
        return self.__id_cliente
    
    @id_cliente.setter
    def id_cliente(self, id_cliente: int):
        if not isinstance(id_cliente, int) or id_cliente < 0:
            raise ValueError("ID do cliente deve ser um número inteiro não negativo.")
        self.__id_cliente = id_cliente
    
    @property
    def bairro(self):
        return self.__bairro
    
    @bairro.setter
    def bairro(self, bairro: str):
        if not bairro.strip():
            raise ValueError("O bairro não pode ser vazio.")
        self.__bairro = bairro
    
    @property
    def cep(self):
        return self.__cep
    
    @cep.setter
    def cep(self, cep: str):
        if not re.match(r'^\d{8}$', cep):
            raise ValueError("CEP deve ter 8 dígitos numéricos.")
        self.__cep = cep
    
    @property
    def rua(self):
        return self.__rua
    
    @rua.setter
    def rua(self, rua: str):
        if not rua.strip():
            raise ValueError("A rua não pode ser vazia.")
        self.__rua = rua
    
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero: str):
        if not re.match(r'^\d+$', numero) and not re.match(r'^[A-Za-z0-9\s]+$', numero):
            raise ValueError("Número deve ser numérico ou uma string válida como 'Apto. 101'.")
        self.__numero = numero

    def to_dict(self):
        return {
            'id': self.id,
            'id_cliente': self.id_cliente,
            'bairro': self.bairro,
            'cep': self.cep,
            'rua': self.rua,
            'numero': self.numero
        }
