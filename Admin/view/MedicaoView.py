from Admin.models import *
from datetime import datetime

class MedicaoView:
    @staticmethod
    def inserir_medicao(id_cliente):
        m = Medicao(
            id_cliente = id_cliente,
            data= datetime.now().strftime("%d/%m/%Y")
        )
        Medicoes.inserir(m)
    
    @staticmethod
    def atualizar_medicao(id, id_cliente, data):
        m = Medicao(
            id=id,
            id_cliente=id_cliente,
            data=data
        )
        Medicoes.atualizar(m)
    
    @staticmethod
    def excluir_medicao(id):
        m = Medicoes.buscar_por_id(id)
        if m is None:
            raise Exception('Medicao Não encontrado')
        Medicoes.excluir(id)
    
    @staticmethod
    def listar_medicoes():
        medicoes = Medicoes.listar()
        medicoes.sort(key=lambda x: datetime.strptime(x.data, '%d/%m/%Y'), reverse=True)
        return medicoes