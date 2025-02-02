from Admin import models

class View:
    @staticmethod
    def inserir_aluno(nome: str, email: str, tel: str, data_cadastro: str, nascimento: str, sexo: str, cpf: str, rg: str, profissao: str):
        aluno = models.Aluno(nome, email, tel, data_cadastro, nascimento, sexo, cpf, rg, profissao)
        models.Alunos.inserir(aluno)

    def listar_alunos():
        return models.Alunos.listar()
