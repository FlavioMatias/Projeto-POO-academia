from Admin.models import *
from datetime import datetime

class TreinoAlunoView:
    @staticmethod
    def inserir_treinoAluno(id_aluno):
        t = TreinoAluno(
            id_aluno = id_aluno,
            data= datetime.now().strftime("%d/%m/%Y")
        )
        TreinosAlunos.inserir(t)
    
    @staticmethod
    def atualizar_treinoAluno(id, id_aluno, data, atv):
        t = TreinoAluno(
            id=id,
            id_aluno=id_aluno,
            data=data,
            atv=atv
        )
        TreinosAlunos.atualizar(t)
    
    @staticmethod
    def excluir_treinoAluno(id):
        ta = None
        for treino in TreinosAlunos.listar():
            if treino.id == id:
                ta = treino
                break
        if ta is None:
            raise Exception('Treino nao encontrado')
        TreinosAlunos.excluir(ta)

    @staticmethod
    def listar_treinos():
        treinos = TreinosAlunos.listar()
        return treinos
    
    @staticmethod
    def buscar_treino(id: int):
        return TreinosAlunos.buscar_por_id(id)
        