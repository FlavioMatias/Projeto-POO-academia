import re
from datetime import datetime

class Aluno:
    def __init__(self,id = 0, nome : str = None, email : str = None, tel : str = None, data_cadastro : str = None, nascimento : str = None, sexo : str = None, cpf : str = None, rg : str = None, profissao : str = None, senha : str = None):
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
        self.senha = senha

    def __str__(self):
        return (f"Aluno ID: {self.id}\n"
                f"Nome: {self.nome}\n"
                f"Email: {self.email}\n"
                f"Telefone: {self.tel}\n"
                f"Data de Cadastro: {self.data_cadastro}\n"
                f"Data de Nascimento: {self.nascimento}\n"
                f"Sexo: {self.sexo}\n"
                f"CPF: {self.cpf}\n"
                f"RG: {self.rg}\n"
                f"Profissão: {self.profissao}")
        
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'senha': self.senha,
            'email': self.email,
            'tel': self.tel,
            'data_cadastro': self.data_cadastro,
            'nascimento': self.nascimento,
            'sexo': self.sexo,
            'cpf': self.cpf,
            'rg': self.rg,
            'profissao': self.profissao
        }
        
    @property
    def id(self): return self.__id
    
    @property
    def nome(self): return self.__nome

    @property
    def email(self): return self.__email
    
    @property
    def tel(self): return self.__tel
    
    @property
    def data_cadastro(self): return self.__data_cadastro
    
    @property
    def nascimento(self): return self.__nascimento
    
    @property
    def sexo(self): return self.__sexo
    
    @property
    def cpf(self): return self.__cpf
    @property
    def rg(self): return self.__rg
    
    @property
    def profissao(self): return self.__profissao

    @id.setter
    def id(self, id: int):
        if not isinstance(id, int):
            raise ValueError("ID do aluno invalido")
        self.__id = id

    @nome.setter
    def nome(self, nome : str):
        ''' Verifica se o nome é uma string, se é menor que 2 letras, se começa com letras minusculas ou se tem simbulos "@,.%"etc. se nao, guarda o nome '''
        
        if not isinstance(nome, str):
            raise ValueError("Nome deve ser uma string.")
        if len(nome) < 3:
            raise ValueError("Nome deve ter pelo menos 2 caracteres.")
        if not re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ]+( [A-Za-zÀ-ÖØ-öø-ÿ]+)*", nome):
            raise ValueError("Nome deve conter apenas letras e espaços simples.")
        if not nome.isalpha() and not nome.replace(" ", "").isalpha():
            raise ValueError("Nome deve conter apenas letras e espaços.")
        if not nome.istitle():
            raise ValueError("Nome deve começar com letra maiúscula.")
        
        self.__nome = nome
        
    @email.setter
    def email(self, email: str):
        if not isinstance(email, str):
            raise ValueError("E-mail deve ser uma string.")
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.fullmatch(regex, email):
            raise ValueError("E-mail inválido. O formato correto é 'exemplo@dominio.com'.")
        self.__email = email
        
    @tel.setter
    def tel(self, tel: str):
        if not isinstance(tel, str):
            raise ValueError("Telefone deve ser uma string.")

        regex = r'^\(?(\d{2})\)?\s?\d{4,5}[-]?\d{4}$'

        match = re.match(regex, tel)
        if not match:
            raise ValueError("Telefone inválido. O formato correto é (XX) XXXXX-XXXX ou (XX) XXXX-XXXX.")

        ddd = int(match.group(1)) 

        ddds_brasil = [
            11, 12, 13, 14, 15, 16, 17, 18, 19,  # SP
            21, 22, 24,  # RJ
            27, 28,  # ES
            31, 32, 33, 34, 35, 37, 38,  # MG
            41, 42, 43, 44, 45, 46,  # PR
            47, 48, 49,  # SC
            51, 53, 54, 55,  # RS
            61,  # DF
            62, 64,  # GO
            63,  # TO
            65, 66,  # MT
            67,  # MS
            68,  # AC
            69,  # RO
            71, 73, 74, 75, 77,  # BA
            79,  # SE
            81, 87,  # PE
            82,  # AL
            83,  # PB
            84,  # RN
            85, 88,  # CE
            86, 89,  # PI
            91, 93, 94,  # PA
            92, 97,  # AM
            95,  # RR
            96,  # AP
            98, 99 # MA
        ]

        if ddd not in ddds_brasil:
            raise ValueError("DDD inválido. O código de área não é válido no Brasil.")

        self.__tel = tel

    @data_cadastro.setter
    def data_cadastro(self, data_cadastro: str):
        try:
            data_obj = datetime.strptime(data_cadastro, '%d/%m/%Y')
        except ValueError:
            raise ValueError("Data de cadastro inválida. Use o formato 'DD/MM/YYYY'.")

        if data_obj > datetime.today():
            raise ValueError("Data de cadastro não pode ser no futuro.")

        self.__data_cadastro = data_cadastro
        
    @nascimento.setter
    def nascimento(self, nascimento: str):
        try:
            data_obj = datetime.strptime(nascimento, '%d/%m/%Y')
            if data_obj > datetime.today():
                raise ValueError("Data de nascimento não pode ser no futuro.")
            self.__nascimento = nascimento
        except ValueError:
            raise ValueError("Data de nascimento inválida. Use o formato 'DD/MM/YYYY'.")
        
    @sexo.setter
    def sexo(self, sexo: str):
        sexo = sexo.upper()
        
        if sexo in ['M', 'F', 'MASCULINO', 'FEMININO', 'OUTRO']:
            self.__sexo = sexo
        else:
            raise ValueError("Sexo inválido.")
        
    @cpf.setter
    def cpf(self, cpf: str):
        cpf = re.sub(r'\D', '', cpf)

        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("CPF deve ter 11 dígitos numéricos.")
        
        if not self.__validar_cpf(cpf):
            raise ValueError("CPF inválido.")
        
        self.__cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        
    @rg.setter
    def rg(self, rg: str):
        rg = re.sub(r'\D', '', rg)
        if len(rg) != 9 or not rg.isdigit():
            raise ValueError("RG deve conter exatamente 9 dígitos numéricos.")
        if rg == rg[0] * 9:
            raise ValueError("RG inválido: sequência numérica repetitiva detectada.")
        self.__rg = rg
    @profissao.setter
    def profissao(self, profissao: str):
        if len(profissao) >= 2 and isinstance(profissao, str):
            if re.search(r'\d', profissao):
                raise ValueError('Profissão não pode conter digitos numéricos.')
            self.__profissao = profissao
        else:
            raise ValueError('Profissão inválida. A profissão deve ter pelo menos 2 caracteres e ser uma string.')
        
    def __validar_cpf(self, cpf: str) -> bool:
        def calcular_digito(cpf: str, peso: list) -> int:
            soma = sum(int(cpf[i]) * peso[i] for i in range(len(peso)))
            resto = soma % 11
            return 0 if resto < 2 else 11 - resto

        if cpf == cpf[0] * 11:
            return False

        peso1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        digito1 = calcular_digito(cpf, peso1)

        peso2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        digito2 = calcular_digito(cpf, peso2)

        return cpf[-2:] == f"{digito1}{digito2}"
    
class Endereco:
    def __init__(self, id=0, id_cliente=0, bairro="", cep="", rua="", numero=""):
        self.id = id
        self.id_cliente = id_cliente
        self.bairro = bairro
        self.cep = cep
        self.rua = rua
        self.numero = numero

    def to_dict(self):
        return {
            'id': self.id,
            'id_cliente': self.id_cliente,
            'bairro': self.bairro,
            'cep': self.cep,
            'rua': self.rua,
            'numero': self.numero
        }
    
    def __str__(self):
        return f"Endereço ID: {self.id}\nCliente ID: {self.id_cliente}\nRua: {self.rua}\nNúmero: {self.numero}\nBairro: {self.bairro}\nCEP: {self.cep}"
    
    # Getters
    @property
    def id(self):
        return self.__id
    
    @property
    def id_cliente(self):
        return self.__id_cliente
    
    @property
    def bairro(self):
        return self.__bairro
    
    @property
    def cep(self):
        return self.__cep
    
    @property
    def rua(self):
        return self.__rua
    
    @property
    def numero(self):
        return self.__numero

    # Setters
    @id.setter
    def id(self, id: int):
        if not isinstance(id, int) or id < 0:
            raise ValueError("ID deve ser um número inteiro não negativo.")
        self.__id = id
    
    @id_cliente.setter
    def id_cliente(self, id_cliente: int):
        if not isinstance(id_cliente, int) or id_cliente < 0:
            raise ValueError("ID do cliente deve ser um número inteiro não negativo.")
        self.__id_cliente = id_cliente
    
    @bairro.setter
    def bairro(self, bairro: str):
        if not bairro.strip():
            raise ValueError("O bairro não pode ser vazio.")
        self.__bairro = bairro
    
    @cep.setter
    def cep(self, cep: str):
        if not re.match(r'^\d{8}$', cep) and not re.match(r'^\d{5}-\d{3}$', cep):
            raise ValueError("CEP deve ter 8 dígitos numéricos.")
        self.__cep = cep
    
    @rua.setter
    def rua(self, rua: str):
        if not rua.strip():
            raise ValueError("A rua não pode ser vazia.")
        self.__rua = rua
    
    @numero.setter
    def numero(self, numero: str):
        if not re.match(r'^\d+$', numero) and not re.match(r'^[A-Za-z0-9\s]+$', numero):
            raise ValueError("Número deve ser numérico ou uma string válida como 'Apto. 101'.")
        self.__numero = numero