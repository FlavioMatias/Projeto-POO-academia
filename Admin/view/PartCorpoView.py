from Admin.models import *

class PartCorpoView:
    @staticmethod
    def inserir_partcorpo(nome, unidade):
        p = PartCorpo(
            nome = nome,
            unidade= unidade
        )
        for partcorpo in PartesCorpo.listar():
            if partcorpo.nome == p.nome:
                raise Exception("Parte do corpo já cadastrada")
        PartesCorpo.inserir(p)
    
    @staticmethod
    def atualizar_partcorpo(id, nome, unidade):
        p = PartCorpo(
            id=id,
            nome = nome,
            unidade= unidade
        )
        PartesCorpo.atualizar(p)
    
    @staticmethod
    def excluir_partcorpo(id):
        p = PartesCorpo.buscar_por_id(id)
        if p is None:
            raise Exception('Parte do corpo Não encontrado')
        PartesCorpo.excluir(id)
    
    @staticmethod
    def listar_partescorpo():
        return PartesCorpo.listar()
    
    @staticmethod
    def buscar_partcorpo(id: int):
        return PartesCorpo.buscar_por_id(id)
    
    @staticmethod
    def inserir_parte_corpo(nm: str, un: str):
        p = PartCorpo(
            nome = nm,
            unidade= un
        )
        PartesCorpo.inserir(p)

    @staticmethod
    def buscar_parte_corpo(id: int):
        partes_corpo = None
        for parte_corpo in PartesCorpo.listar():
            if parte_corpo.id == id:
                partes_corpo = parte_corpo
        return partes_corpo
    
    @staticmethod
    def excluir_parte_corpo(id: int):
        parte = None
        for parte_corpo in PartesCorpo.listar():
            if parte_corpo.id == id:
                parte = parte_corpo
                break
        if parte is None:
            raise Exception('Parte do corpo nao encontrada')
        PartesCorpo.excluir(parte)