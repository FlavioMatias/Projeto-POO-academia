from Admin import models
import re

class View:
    @staticmethod
    def inserir_aluno(nome: str, email: str, tel: str, data_cadastro: str, nascimento: str, sexo: str, cpf: str, rg: str, profissao: str, bairro : str, cep : str, rua : str, numero : int):
        aluno = models.Aluno(0, nome, email, tel, data_cadastro, nascimento, sexo, cpf, rg, profissao)
        l = models.Alunos.listar()
        print(re.sub(r'\D', '', cpf))
        liberado = True 
        for alu in l:
            if alu.cpf == re.sub(r'\D', '', cpf):
                liberado = False

        if liberado:        
            models.Alunos.inserir(aluno)
        else:
            raise ValueError('cpf ja cadastrado')

        la = models.Alunos.listar()

        for alu in la:
            if alu.cpf == re.sub(r'\D', '', cpf):
                endereço = models.Endereco(0, alu.id, bairro, cep, rua, numero)
                models.Enderecos.inserir(endereço)
            else:
                print('cpf nao adcionado')

    def listar_alunos():
        return models.Alunos.listar()
    
    def listar_endereços():
        endere = models.Enderecos.listar()
        print('le', endere)
        return endere
        
