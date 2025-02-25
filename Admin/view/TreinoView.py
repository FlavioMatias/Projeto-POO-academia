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
        t = None
        for treino in Treinos.listar():
            if treino.id == id:
                t = treino
                break
        if t is None:
            raise Exception('Treino nao encontrado')
        Treinos.excluir(t)
    
    @staticmethod
    def listar_treinos():
        return Treinos.listar()
    
    @staticmethod
    def buscar_treino(id: int):
        return Treinos.buscar_por_id(id)
    
    @staticmethod
    def listar_treino_do_treinoaluno(id_treino):
        treinos = []
        for t in Treinos.listar():
            if t.id_treino == id_treino:
                treinos.append(t)
        return treinos
    
    @staticmethod
    def buscar_treino_por_id_musculo(id_musculo):
        a = None
        for treino in Treinos.listar():
            if treino.id_musculo == id_musculo:
                a = treino
                break
        return a