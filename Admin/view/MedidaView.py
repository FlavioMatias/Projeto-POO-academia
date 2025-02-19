from Admin.models import *
from datetime import datetime


class MedidaView:
    @staticmethod
    def inserir_medida(id_medicoes, id_partcorpo, valor):
        m = Medida(
            id_medicoes = id_medicoes,
            id_partcorpo=id_partcorpo,
            valor = valor
        )
        Medidas.inserir(m)
    @staticmethod
    def atualizar_medida(id, id_medicoes, id_partcorpo, valor):
        m = Medida(
            id=id,
            id_medicoes=id_medicoes,
            id_partcorpo=id_partcorpo,
            valor=valor
        )
        Medidas.atualizar(m)
    @staticmethod
    def excluir_medida(id):
        m = Medidas.buscar_por_id(id)
        if m is None:
            raise Exception('Medida Não encontrado')
        Medidas.excluir(id)
    
    @staticmethod
    def listar_medidas():
        return Medidas.listar()
    
    def buscar_medida(id: int):
        return Medidas.buscar_por_id(id)