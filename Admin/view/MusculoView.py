from Admin.models import *

class MusculoView:
    @staticmethod
    def inserir_musculo(nome):
        m = Musculo(
            nome = nome
        )
        for musculo in Musculos.listar():
            if musculo.nome == m.nome:
                raise Exception("Musculo já cadastrado")
        Musculos.inserir(m)
    
    @staticmethod
    def atualizar_musculo(id, nome):
        m = Musculo(
            id=id,
            nome = nome
        )
        Musculos.atualizar(m)
    
    @staticmethod
    def excluir_musculo(id):
        m = Musculos.buscar_por_id(id)
        if m is None:
            raise Exception('Musculo Não encontrado')
        Musculos.excluir(id)

    @staticmethod
    def listar_musculos():
        return Musculos.listar()
    
    @staticmethod
    def buscar_musculo(id: int):
        musculos = []
        for musculo in Musculos.listar():
            if musculo.id == id:
                musculos.append(musculo)
        return musculos