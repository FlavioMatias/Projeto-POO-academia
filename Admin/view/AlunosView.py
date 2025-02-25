from Admin.models import *


class AlunosView:
    @staticmethod
    def inserir_aluno(nm: str, cpf : str, email: str, senha: str, tel: str, dtCad: str, dtNasc: str, sexo: str, rg: str, prof: str, bairro: str, cep: str, rua: str, num: str):
        a = Aluno(
            nome = nm,
            email = email,
            senha = senha,
            tel = tel,
            data_cadastro = dtCad,
            cpf = cpf,
            nascimento = dtNasc,
            sexo = sexo,
            rg = rg,
            profissao = prof
            )
        liberar_inserção = True

        for cpf in Alunos.listar():
            if cpf == a.cpf:
                liberar_inserção = False

        if liberar_inserção:
            Alunos.inserir(a)
        else:
            raise Exception("CPF já cadastrado")
        try:
            e = Endereco(
                id_cliente= a.id,
                bairro = bairro,
                cep = cep,
                rua = rua,
                numero = num
                )
            Enderecos.inserir(e)
        except Exception as e:
            Alunos.excluir(a)
            raise ValueError (e)
    
    @staticmethod
    def Atualizar_aluno(id: int, nm: str, cpf : str, email: str, senha: str, tel: str, dtCad: str, dtNasc: str, sexo: str, rg: str, prof: str, bairro: str, cep: str, rua: str, num: str):
        a = Aluno(
            id = id,
            nome = nm,
            email = email,
            senha = senha,
            tel = tel,
            data_cadastro = dtCad,
            cpf = cpf,
            nascimento = dtNasc,
            sexo = sexo,
            rg = rg,
            profissao = prof
            )
        Alunos.atualizar(a)

        for endereco in Enderecos.listar():
            if endereco.id_cliente == id:
                id_endereço = endereco.id
            else:
                id_endereço = False

        if id_endereço: 
            e = Endereco(
                id = id_endereço,
                id_cliente= a.id,
                bairro = bairro,
                cep = cep,
                rua = rua,
                numero = num
                )
            Enderecos.atualizar(e)
    
    @staticmethod
    def excluir_aluno(id: int):
        a = Alunos.buscar_por_id(id)
        Alunos.excluir(a)
        for endereco in Enderecos.listar():
            if endereco.id_cliente == id:
                Enderecos.excluir(endereco)

    @staticmethod
    def listar_alunos():
        return Alunos.listar()
    
    @staticmethod
    def buscar_aluno(id: int):
        return Alunos.buscar_por_id(id) 
    
    @staticmethod
    def buscar_endereco_aluno(id: int):
        for endereco in Enderecos.listar():
            if endereco.id_cliente == id:
                return endereco
        return None
    @staticmethod
    def buscar_matricula_aluno(id: int):
        for matricula in Matriculas.listar():
            if matricula.id_aluno == id and not matricula.ativa:
                return matricula
        return None
    