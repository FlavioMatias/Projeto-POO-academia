from App import models
import re
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
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
            la = models.Alunos.listar()

            for alu in la:
                if alu.cpf == re.sub(r'\D', '', cpf):
                    endereço = models.Endereco(0, alu.id, bairro, cep, rua, numero)
                    models.Enderecos.inserir(endereço)
                    
                else:
                    raise ValueError('cpf ja cadastrado')
            else:
                print('endereço nao adcionado')




    def listar_alunos():
        return models.Alunos.listar()
    
    def listar_endereços():
        endere = models.Enderecos.listar()
        return endere
    
    def listar_planos():
        return models.Planos.listar()
    
    def listar_matriculas():
        return models.Matriculas.listar()
    
    @classmethod
    def inserir_matricula(cls, id_aluno, id_plano, data, validade):
        print(f'id do aluno no inserir matricula: {id_aluno}')
        
        m = models.Matricula(0, id_aluno, id_plano, data, cls.calcular_validade(data, validade))
        matriculas = models.Matriculas.listar()
        liberado = True
        for matricula in matriculas:
            if matricula.id_cliente == id_aluno:
                liberado = False
        if liberado:
            models.Matriculas.inserir(m)
        else:
            raise ValueError('cliente ja esta matriculado')

    @classmethod
    def calcular_validade(cls, data_inicial, tempo):
        # Converter data_inicial para datetime se for string
        if isinstance(data_inicial, str):
            data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y')

        quantidade, unidade = tempo.split()  # Ex: "3 meses" → quantidade="3", unidade="meses"
        quantidade = int(quantidade)

        if "semana" in unidade:  # Para semanas
            data_validade = data_inicial + relativedelta(weeks=quantidade)
        elif "mês" in unidade:  # Para meses
            data_validade = data_inicial + relativedelta(months=quantidade)
        elif "ano" in unidade:  # Para anos
            data_validade = data_inicial + relativedelta(years=quantidade)
        else:
            data_validade = data_inicial  # Caso inesperado

        return data_validade.strftime('%d/%m/%Y')