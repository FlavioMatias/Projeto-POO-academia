from Admin.models import *

class TreinoView:
    @staticmethod
    def inserir_treino(id_musculo, id_treino, descricao=""):
        t = Treino(
            id_musculo=id_musculo,
            id_treino=id_treino,
            descricao=descricao
        )
        Treinos.inserir(t)
        
    @staticmethod
    def atualizar_treino(id, id_musculo, id_treino, descricao=""):
        t = Treino(
            id=id,
            id_musculo=id_musculo,
            id_treino=id_treino,
            descricao=descricao
        )
        Treinos.atualizar(t)
    
    @staticmethod
    def excluir_treino(id):
        t = Treinos.buscar_por_id(id)
        if t is None:
            raise Exception('Treino Não encontrado')
        Treinos.excluir(id)
    
    @staticmethod
    def listar_treinos():
        return Treinos.listar()
    
    @staticmethod
    def buscar_treino(id: int):
        return Treinos.buscar_por_id(id)