import json

from Admin.models.matricula import Matricula
from Admin.models.alunos import Aluno, Endereco
from Admin.models.plano import Plano
from Admin.models.pagamento import Pagamento
from Admin.models.medicao import Medicao, Medida, PartCorpo
from Admin.models.treino import TreinoAluno,Treino


class CRUD:
    objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for x in cls.objetos:
            if x.id > id: id = x.id
        obj.id = id + 1    
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    @classmethod
    def listar_id(cls, id):
        cls.abrir()

        for x in cls.objetos:
            if x.id == id: return x
        return None
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()        
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
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
    objetos = []
    
    @classmethod
    def salvar(cls):
        with open("data/matriculas.json", mode="w") as arquivo:
            json.dump([vars(obj) for obj in cls.objetos], arquivo)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("data/matriculas.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                
                for obj in objetos_json:
                    A = Matricula(
                        obj["id"], obj["id_cliente"], obj.get("plano", ""),
                        obj.get("data", ""), obj.get("validade", "")
                    )
                    cls.objetos.append(A)
        except FileNotFoundError:
            pass

class Alunos(CRUD):
    @classmethod
    def salvar(cls):
        with open("Data/alunos.json", mode="w") as arquivo:
            dados = [aluno.to_dict() for aluno in cls.objetos]
            json.dump(dados, arquivo, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Data/alunos.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)

                for obj in objetos_json:
                    A = Aluno(
                        obj["id"], obj["nome"], obj.get("email", ""), obj.get("tel", ""),
                        obj["data_cadastro"], obj.get("nascimento", ""), obj.get("sexo", ""),
                        obj.get("cpf", ""), obj.get("rg", ""), obj.get("profissao", "")
                    )
                    cls.objetos.append(A)    

        except FileNotFoundError:
            pass

class Enderecos(CRUD):
    objetos = []
    
    @classmethod
    def salvar(cls):
        with open("data/enderecos.json", mode="w") as arquivo:
            json.dump([vars(obj) for obj in cls.objetos], arquivo)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("data/enderecos.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                
                for obj in objetos_json:
                    A = Endereco(
                        obj["id"], obj["id_cliente"], obj.get("bairro", ""),
                        obj.get("cep", ""), obj.get("rua", ""), obj.get("numero", "")
                    )
                    cls.objetos.append(A)
        except FileNotFoundError:
            pass

class Planos(CRUD):
    @classmethod
    def salvar(cls):
        with open("data/planos.json", mode="w") as arquivo:
            json.dump([vars(obj) for obj in cls.objetos], arquivo)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("data/planos.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                
                for obj in objetos_json:
                    A = Plano(
                        obj["id"], obj["nome"], obj.get("valor", 0.0), obj.get("tempo", "")
                    )
                    cls.objetos.append(A)
        except FileNotFoundError:
            pass

class Pagamentos(CRUD):
    @classmethod
    def salvar(cls):
        with open("data/pagamentos.json", mode="w") as arquivo:
            json.dump([vars(obj) for obj in cls.objetos], arquivo)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("data/pagamentos.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                
                for obj in objetos_json:
                    P = Pagamento(
                        obj["id"], obj["id_matricula"], obj["id_cliente"], obj.get("emissao", ""),
                        obj.get("vencimento", ""), obj.get("data_pagamento", ""), obj.get("valor", 0.0), obj.get("pago", False)
                    )
                    cls.objetos.append(P)
        except FileNotFoundError:
            pass

class Medicoes(CRUD):
    @classmethod
    def salvar(cls):
        with open("data/medicoes.json", mode="w") as arquivo:
            json.dump([vars(obj) for obj in cls.objetos], arquivo)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("data/medicoes.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                
                for obj in objetos_json:
                    M = Medicao(
                        obj["id"], obj["id_cliente"], obj.get("data", "")
                    )
                    cls.objetos.append(M)
        except FileNotFoundError:
            pass

class Medidas(CRUD):
    @classmethod
    def salvar(cls):
        with open("data/medidas.json", mode="w") as arquivo:
            json.dump([vars(obj) for obj in cls.objetos], arquivo)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("data/medidas.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                
                for obj in objetos_json:
                    M = Medida(
                        obj["id"], obj["id_medicoes"], obj["id_partcorpo"], obj.get("valor", 0.0)
                    )
                    cls.objetos.append(M)
        except FileNotFoundError:
            pass

class PartesCorpo(CRUD):
    @classmethod
    def salvar(cls):
        with open("data/partcorpos.json", mode="w") as arquivo:
            json.dump([vars(obj) for obj in cls.objetos], arquivo)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("data/partcorpos.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                
                for obj in objetos_json:
                    P = PartCorpo(
                        obj["id"], obj.get("nome", ""), obj.get("unidade", "")
                    )
                    cls.objetos.append(P)
        except FileNotFoundError:
            pass
class TreinosAlunos:
    @classmethod
    def salvar(cls):
        with open("data/treinoaluno.json", mode="w") as arquivo:
            json.dump([vars(obj) for obj in cls.objetos], arquivo)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("data/treinoaluno.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                
                for obj in objetos_json:
                    T = TreinoAluno(
                        obj["id"], obj["id_aluno"], obj.get("data", ""), obj.get("data_final", "")
                    )
                    cls.objetos.append(T)
        except FileNotFoundError:
            pass

class Treinos(CRUD):
    @classmethod
    def salvar(cls):
        with open("data/treinos.json", mode="w") as arquivo:
            json.dump([vars(obj) for obj in cls.objetos], arquivo)
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("data/treinos.json", mode="r") as arquivo:
                objetos_json = json.load(arquivo)
                
                for obj in objetos_json:
                    T = Treino(
                        obj["id"], obj["id_musculo"], obj.get("id_treino", 0), obj.get("descricao", "")
                    )
                    cls.objetos.append(T)
        except FileNotFoundError:
            pass
