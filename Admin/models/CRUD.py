import json

from Admin.models.matricula import Matricula
from Admin.models.alunos import Aluno, Endereco
from Admin.models.plano import Plano
from Admin.models.pagamento import Pagamento
from Admin.models.medicao import Medicao, Medida, PartCorpo
from Admin.models.treino import TreinoAluno,Treino, Musculo

#from matricula import Matricula
#from alunos import Aluno, Endereco
#from plano import Plano
#from pagamento import Pagamento
#from medicao import Medicao, Medida, PartCorpo
#from treino import TreinoAluno,Treino, Musculo

class CRUD:
    
    objetos = []
    
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for x in cls.objetos:
            if x.id > id:
                id = x.id
                
        obj.id = id + 1
        
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def buscar_por_id(cls, id):
        
        cls.abrir()
        for x in cls.objetos:
            if x.id == id:
                return x
        return None

    @classmethod
    def atualizar(cls, obj):
        x = cls.buscar_por_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()    
                
    @classmethod
    def excluir(cls, obj):
        x = cls.buscar_por_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()
            
    @classmethod
    def abrir():
        pass

    @classmethod
    def salvar():
        pass

class Matriculas(CRUD):
    @classmethod
    def salvar(cls):
        with open("Data/matriculas.json", mode="w") as arquivo:
            dados = [matricula.to_dict() for matricula in cls.objetos]
            json.dump(dados, arquivo)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Data/matriculas.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                
                for obj in objetos_json:
                    M = Matricula(
                        obj["id"], obj["id_aluno"], obj.get("plano", ""),
                        obj.get("data", ""), obj.get("validade", ""),obj.get("ativa", False)
                    )
                    cls.objetos.append(M)
        except FileNotFoundError as e:
            print(e) 

class Alunos(CRUD):
    @classmethod
    def salvar(cls):
        with open("Data/alunos.json", mode="w") as arquivo:
            dados = [aluno.to_dict() for aluno in cls.objetos]
            json.dump(dados, arquivo)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Data/alunos.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)

                for obj in objetos_json:
                    print(obj["nome"])
                    A = Aluno(
                        obj["id"], obj["nome"], obj.get("email", ""), obj.get("tel", ""),
                        obj["data_cadastro"], obj.get("nascimento", ""), obj.get("sexo", ""),
                        obj.get("cpf", ""), obj.get("rg", ""), obj.get("profissao", ""), obj["senha"]
                    )
                    cls.objetos.append(A)    

        except FileNotFoundError as e:
            print(e)

class Enderecos(CRUD):
    @classmethod
    def salvar(cls):
        with open("Data/enderecos.json", mode="w") as arquivo:
            dados = [endereco.to_dict() for endereco in cls.objetos]
            json.dump(dados, arquivo)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Data/enderecos.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                
                for obj in objetos_json:
                    E = Endereco(
                        obj["id"], obj["id_cliente"], obj.get("bairro", ""),
                        obj.get("cep", ""), obj.get("rua", ""), obj.get("numero", "")
                    )
                    cls.objetos.append(E)
        except FileNotFoundError as e:
            print(e) 

class Planos(CRUD):
    @classmethod
    def salvar(cls):
        with open("Data/planos.json", mode="w") as arquivo:
            dados = [plano.to_dict() for plano in cls.objetos]
            json.dump(dados, arquivo)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Data/planos.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                
                for obj in objetos_json:
                    P = Plano(
                        obj["id"], obj["nome"], obj.get("valor", 0.0), obj.get("tempo", "")
                    )
                    cls.objetos.append(P)
        except FileNotFoundError as e:
            print(e) 

class Pagamentos(CRUD):
    @classmethod
    def salvar(cls):
        with open("Data/pagamentos.json", mode="w") as arquivo:
            dados = [pagamento.to_dict() for pagamento in cls.objetos]
            json.dump(dados, arquivo)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Data/pagamentos.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                
                for obj in objetos_json:
                    P = Pagamento(
                        obj["id"], obj["id_matricula"], obj["id_cliente"], obj.get("emissao", ""),
                        obj.get("vencimento", ""), obj.get("data_pagamento", ""), obj.get("valor", 0.0), obj.get("pago", False)
                    )
                    cls.objetos.append(P)
        except FileNotFoundError as e:
            print(e) 

class Medicoes(CRUD):
    @classmethod
    def salvar(cls):
        with open("Data/medicoes.json", mode="w") as arquivo:
            dados = [medicao.to_dict() for medicao in cls.objetos]
            json.dump(dados, arquivo)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Data/medicoes.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                
                for obj in objetos_json:
                    M = Medicao(
                        obj["id"], obj["id_cliente"], obj.get("data", "")
                    )
                    cls.objetos.append(M)
        except FileNotFoundError as e:
            print(e) 

class Medidas(CRUD):
    @classmethod
    def salvar(cls):
        with open("Data/medidas.json", mode="w") as arquivo:
            dados = [medida.to_dict() for medida in cls.objetos]
            json.dump(dados, arquivo)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Data/medidas.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                
                for obj in objetos_json:
                    M = Medida(
                        obj["id"], obj["id_medicoes"], obj["id_partcorpo"], obj.get("valor", 0.0)
                    )
                    cls.objetos.append(M)
        except FileNotFoundError as e:
            print(e) 

class PartesCorpo(CRUD):
    @classmethod
    def salvar(cls):
        with open("Data/partcorpos.json", mode="w") as arquivo:
            dados = [partcorpo.to_dict() for partcorpo in cls.objetos]
            json.dump(dados, arquivo)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Data/partcorpos.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                
                for obj in objetos_json:
                    P = PartCorpo(
                        obj["id"], obj.get("nome", ""), obj.get("unidade", "")
                    )
                    cls.objetos.append(P)
        except FileNotFoundError as e:
            print(e) 

class TreinosAlunos(CRUD):
    @classmethod
    def salvar(cls):
        with open("Data/treinoaluno.json", mode="w") as arquivo:
            dados = [treino_aluno.to_dict() for treino_aluno in cls.objetos]
            json.dump(dados, arquivo)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Data/treinoaluno.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                
                for obj in objetos_json:
                    T = TreinoAluno(
                        obj["id"], obj["id_aluno"], obj.get("data", ""), obj.get("ativa", False)
                    )
                    cls.objetos.append(T)
        except FileNotFoundError as e:
            print(e) 

class Treinos(CRUD):
    @classmethod
    def salvar(cls):
        with open("Data/treinos.json", mode="w") as arquivo:
            dados = [treino.to_dict() for treino in cls.objetos]
            json.dump(dados, arquivo)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Data/treinos.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                
                for obj in objetos_json:
                    T = Treino(
                        obj["id"], obj["id_musculo"], obj.get("id_treino", 0), obj.get("descricao", "")
                    )
                    cls.objetos.append(T)
        except FileNotFoundError as e:
            print(e) 

class Musculos(CRUD):
    @classmethod
    def salvar(cls):
        with open("Data/musculos.json", mode="w") as arquivo:
            dados = [musculo.to_dict() for musculo in cls.objetos]
            json.dump(dados, arquivo)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Data/musculos.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                
                for obj in objetos_json:
                    M = Musculo(obj["id"], obj["nome"])
                    cls.objetos.append(M)
        except FileNotFoundError as e:
            print(e) 

