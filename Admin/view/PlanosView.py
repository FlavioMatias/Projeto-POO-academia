from Admin.models import *

class PlanosView:
    @staticmethod
    def inserir_plano(nome: str, valor: float, tempo: str):
        p = Plano(
            nome = nome,
            valor = valor,
            tempo = tempo
        )
        for plano in Planos.listar():
            if plano.nome == p.nome and plano.tempo == p.tempo and plano.valor == p.valor:
                raise Exception("Plano já cadastrado")
        Planos.inserir(p)

    
    @staticmethod
    def atualizar_plano(id: int, nome: str, valor: float, tempo: str):
        p = Plano(
            id = id,
            nome = nome,
            valor = valor,
            tempo = tempo
        )
        Planos.atualizar(p)
    
    @staticmethod
    def excluir_plano(id: int):
        p = Planos.buscar_por_id(id)
        if p is None:
            raise Exception('plano Não encontrado')
        Planos.excluir(id)
    
    @staticmethod
    def listar_planos():
        return Planos.listar()
    
    @staticmethod
    def buscar_plano(id: int):
        planos = None
        for plano in Planos.listar():
            if plano.id == id:
                planos = plano
        return planos
    

        