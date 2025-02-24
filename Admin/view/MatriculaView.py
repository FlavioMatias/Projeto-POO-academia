from Admin.models import *
import re
from dateutil.relativedelta import relativedelta
from datetime import datetime

class MatriculaView:
    @staticmethod
    def inserir_matricula(id_aluno, plano, data):
        plano_encontrado = False
        for p in Planos.listar():
            if p.id == plano:
                tempo_plano = p.tempo
                plano_encontrado = True
                break
                
        if not plano_encontrado:
            raise ValueError('Plano não encontrado')
        
        padrao = r"(\d+)\s*(ano|anos|mes|meses|semana|semanas)"
        match = re.match(padrao, tempo_plano)

        quantidade = int(match.group(1))
        unidade = match.group(2).lower()

        unidades_map = {
            'ano': 'years',
            'anos': 'years',
            'mes': 'months',
            'meses': 'months',
            'semana': 'weeks',
            'semanas': 'weeks'
        }

        if unidade not in unidades_map:
            raise ValueError(f'Unidade de tempo "{unidade}" não reconhecida')

        data_dt = datetime.strptime(data, '%d/%m/%Y')
        tempo_plano = {unidades_map[unidade]: quantidade}

        validade = data_dt + relativedelta(**tempo_plano)

        m = Matricula(
            id=0,
            id_aluno=id_aluno,
            plano=plano,
            data=data,
            validade=validade.strftime('%d/%m/%Y')
        )

        for matricula in Matriculas.listar():
            if matricula.id_aluno == id_aluno and matricula.ativa:
                raise Exception('Já existe uma matrícula ativa para esse aluno')
        
        Matriculas.inserir(m)
        
    @staticmethod
    def atualizar_matricula(id, id_aluno, plano, data, validade, ativa):
        m = Matricula(
            id=id,
            id_aluno=id_aluno,
            plano=plano,
            data=data,
            validade=validade,
            ativa=ativa
        )
        Matriculas.atualizar(m)

    @staticmethod
    def excluir_matricula(id: int):
        m = Matriculas.buscar_por_id(id)
        if m is None:
            raise Exception('Matrícula não encontrada')
        Matriculas.excluir(m)

    @staticmethod
    def listar_matriculas():
        return Matriculas.listar()
    
    @staticmethod
    def buscar_matricula(id: int):
        matriculas = []
        for matricula in Matriculas.listar():
            if matricula.id == id:
                matriculas.append(matricula)


        return matriculas
    
