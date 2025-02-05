import sqlite3

from App.models.matricula import Matricula
from App.models.aluno import Aluno, Endereco
from App.models.plano import Plano
from App.models.pagamento import Pagamento
from App.models.medicao import Medicao, Medida, PartCorpo
from App.models.treino import TreinoAluno,Treino, Musculo

class CRUD:
    objetos = []

    @classmethod
    def get_connection(cls):
        return sqlite3.connect('Data/academia.db')
    
    @classmethod
    def tabela(cls):
        return cls.__name__.lower() 
    
    @classmethod
    def limpar(cls):
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(f'DELETE FROM {cls.tabela()};')
        connection.commit()
        cursor.close()
        connection.close()


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
    @classmethod
    def salvar(cls):
        cls.limpar()
        connection = cls.get_connection()
        cursor = connection.cursor()

        for matricula in cls.objetos:
            dados = matricula.to_dict()
            cursor.execute(
                f'INSERT INTO {cls.tabela()} (id, id_cliente, plano, data, validade) VALUES (?, ?, ?, ?, ?)',
                (dados["id"], dados["id_cliente"], dados["plano"], dados["data"], dados["validade"])
            )

        connection.commit()
        cursor.close()
        connection.close()
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {cls.tabela()}')
        registros = cursor.fetchall()
        for reg in registros:
            M = Matricula(reg[0], reg[1], reg[2], reg[3], reg[4])
            cls.objetos.append(M)

        cursor.close()
        connection.close()

class Alunos(CRUD):
    @classmethod
    def salvar(cls):
        cls.limpar()
        connection = cls.get_connection()
        cursor = connection.cursor()

        for aluno in cls.objetos:
            dados = aluno.to_dict()
            cursor.execute(
                f'INSERT INTO {cls.tabela()} (id, nome, email, tel, data_cadastro, nascimento, sexo, cpf, rg, profissao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (dados["id"], dados["nome"], dados.get("email", ""), dados.get("tel", ""), dados["data_cadastro"], dados.get("nascimento", ""), dados.get("sexo", ""), dados.get("cpf", ""), dados.get("rg", ""), dados.get("profissao", ""))
            )

        connection.commit()
        cursor.close()
        connection.close()
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {cls.tabela()}')
        registros = cursor.fetchall()
        for reg in registros:
            A = Aluno(reg[0], reg[1], reg[2], reg[3], reg[4], reg[5], reg[6], reg[7], reg[8], reg[9])
            cls.objetos.append(A)

        cursor.close()
        connection.close()

class Enderecos(CRUD):
    @classmethod
    def salvar(cls):
        cls.limpar()
        connection = cls.get_connection()
        cursor = connection.cursor()

        for endereco in cls.objetos:
            dados = endereco.to_dict()
            cursor.execute(
                f'INSERT INTO {cls.tabela()} (id, id_cliente, bairro, cep, rua, numero) VALUES (?, ?, ?, ?, ?, ?)',
                (dados["id"], dados["id_cliente"], dados.get("bairro", ""), dados.get("cep", ""), dados.get("rua", ""), dados.get("numero", ""))
            )

        connection.commit()
        cursor.close()
        connection.close()
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {cls.tabela()}')
        registros = cursor.fetchall()
        for reg in registros:
            E = Endereco(reg[0], reg[1], reg[2], reg[3], reg[4], reg[5])
            cls.objetos.append(E)

        cursor.close()
        connection.close()

class Planos(CRUD):
    @classmethod
    def salvar(cls):
        cls.limpar()
        connection = cls.get_connection()
        cursor = connection.cursor()

        for plano in cls.objetos:
            dados = plano.to_dict()
            cursor.execute(
                f'INSERT INTO {cls.tabela()} (id, nome, valor, tempo) VALUES (?, ?, ?, ?)',
                (dados["id"], dados["nome"], dados.get("valor", 0.0), dados.get("tempo", ""))
            )

        connection.commit()
        cursor.close()
        connection.close()
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {cls.tabela()}')
        registros = cursor.fetchall()
        for reg in registros:
            P = Plano(reg[0], reg[1], reg[2], reg[3])
            cls.objetos.append(P)

        cursor.close()
        connection.close()

class Pagamentos(CRUD):
    @classmethod
    def salvar(cls):
        cls.limpar()
        connection = cls.get_connection()
        cursor = connection.cursor()

        for pagamento in cls.objetos:
            dados = pagamento.to_dict()
            cursor.execute(
                f'INSERT INTO {cls.tabela()} (id, id_matricula, id_cliente, emissao, vencimento, data_pagamento, valor, pago) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                (dados["id"], dados["id_matricula"], dados["id_cliente"], dados.get("emissao", ""), dados.get("vencimento", ""), dados.get("data_pagamento", ""), dados.get("valor", 0.0), dados.get("pago", False))
            )

        connection.commit()
        cursor.close()
        connection.close()
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {cls.tabela()}')
        registros = cursor.fetchall()
        for reg in registros:
            P = Pagamento(reg[0], reg[1], reg[2], reg[3], reg[4], reg[5], reg[6], reg[7])
            cls.objetos.append(P)

        cursor.close()
        connection.close()

class Medicoes(CRUD):
    @classmethod
    def salvar(cls):
        cls.limpar()
        connection = cls.get_connection()
        cursor = connection.cursor()

        for medicao in cls.objetos:
            dados = medicao.to_dict()
            cursor.execute(
                f'INSERT INTO {cls.tabela()} (id, id_cliente, data) VALUES (?, ?, ?)',
                (dados["id"], dados["id_cliente"], dados.get("data", ""))
            )

        connection.commit()
        cursor.close()
        connection.close()
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {cls.tabela()}')
        registros = cursor.fetchall()
        for reg in registros:
            M = Medicao(reg[0], reg[1], reg[2])
            cls.objetos.append(M)

        cursor.close()
        connection.close()

class Medidas(CRUD):
    @classmethod
    def salvar(cls):
        cls.limpar()
        connection = cls.get_connection()
        cursor = connection.cursor()

        for medida in cls.objetos:
            dados = medida.to_dict()
            cursor.execute(
                f'INSERT INTO {cls.tabela()} (id, id_medicoes, id_partcorpo, valor) VALUES (?, ?, ?, ?)',
                (dados["id"], dados["id_medicoes"], dados["id_partcorpo"], dados.get("valor", 0.0))
            )

        connection.commit()
        cursor.close()
        connection.close()
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {cls.tabela()}')
        registros = cursor.fetchall()
        for reg in registros:
            M = Medida(reg[0], reg[1], reg[2], reg[3])
            cls.objetos.append(M)

        cursor.close()
        connection.close()

class PartesCorpo(CRUD):
    @classmethod
    def salvar(cls):
        cls.limpar()
        connection = cls.get_connection()
        cursor = connection.cursor()

        for partcorpo in cls.objetos:
            dados = partcorpo.to_dict()
            cursor.execute(
                f'INSERT INTO {cls.tabela()} (id, nome, unidade) VALUES (?, ?, ?)',
                (dados["id"], dados.get("nome", ""), dados.get("unidade", ""))
            )

        connection.commit()
        cursor.close()
        connection.close()
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {cls.tabela()}')
        registros = cursor.fetchall()
        for reg in registros:
            P = PartCorpo(reg[0], reg[1], reg[2])
            cls.objetos.append(P)

        cursor.close()
        connection.close()

class TreinosAlunos(CRUD):
    @classmethod
    def salvar(cls):
        cls.limpar()
        connection = cls.get_connection()
        cursor = connection.cursor()

        for treino_aluno in cls.objetos:
            dados = treino_aluno.to_dict()
            cursor.execute(
                f'INSERT INTO {cls.tabela()} (id, id_aluno, data, data_final) VALUES (?, ?, ?, ?)',
                (dados["id"], dados["id_aluno"], dados.get("data", ""), dados.get("data_final", ""))
            )

        connection.commit()
        cursor.close()
        connection.close()
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {cls.tabela()}')
        registros = cursor.fetchall()
        for reg in registros:
            T = TreinoAluno(reg[0], reg[1], reg[2], reg[3])
            cls.objetos.append(T)

        cursor.close()
        connection.close()

class Treinos(CRUD):
    @classmethod
    def salvar(cls):
        cls.limpar()
        connection = cls.get_connection()
        cursor = connection.cursor()

        for treino in cls.objetos:
            dados = treino.to_dict()
            cursor.execute(
                f'INSERT INTO {cls.tabela()} (id, id_musculo, id_treino, descricao) VALUES (?, ?, ?, ?)',
                (dados["id"], dados["id_musculo"], dados.get("id_treino", 0), dados.get("descricao", ""))
            )

        connection.commit()
        cursor.close()
        connection.close()
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {cls.tabela()}')
        registros = cursor.fetchall()
        for reg in registros:
            T = Treino(reg[0], reg[1], reg[2], reg[3])
            cls.objetos.append(T)

        cursor.close()
        connection.close()

class Musculos(CRUD):
    @classmethod
    def salvar(cls):
        cls.limpar()
        connection = cls.get_connection()
        cursor = connection.cursor()

        for musculo in cls.objetos:
            dados = musculo.to_dict()
            cursor.execute(
                f'INSERT INTO {cls.tabela()} (id, nome) VALUES (?, ?)',
                (dados["id"], dados["nome"])
            )

        connection.commit()
        cursor.close()
        connection.close()
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(f'SELECT * FROM {cls.tabela()}')
        registros = cursor.fetchall()
        for reg in registros:
            M = Musculo(reg[0], reg[1])
            cls.objetos.append(M)

        cursor.close()
        connection.close()
