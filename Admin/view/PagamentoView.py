from Admin.models import *
from datetime import datetime
from dateutil.relativedelta import relativedelta

class PagamentoView:
    @staticmethod
    def inserir_pagamento(id_matricula, id_cliente, intervalo_meses = 1):
        emissao = datetime.now().strftime("%d/%m/%Y")
        data_atual = datetime.strptime(emissao, "%d/%m/%Y")
        nova_data = data_atual + relativedelta(months=intervalo_meses)
        vencimento = nova_data.strftime("%d/%m/%Y")

        for m in Matriculas.listar():
            if m.id == id_matricula and m.ativa:
                valor = Planos.buscar_por_id(m.plano).valor
                break

        p = Pagamento(
            id_matricula=id_matricula,
            id_cliente=id_cliente,
            emissao=emissao,
            vencimento=vencimento,
            valor=valor,
            pago=False
        )
        Pagamentos.inserir(p)

    @staticmethod
    def atualizae_pagamento(id, id_matricula, id_cliente, emissao, vencimento, data_pagamento, valor, pago):
        p = Pagamento(
            id=id,
            id_matricula=id_matricula,
            id_cliente=id_cliente,
            emissao=emissao,
            vencimento=vencimento,
            data_pagamento=data_pagamento,
            valor=valor,
            pago=pago
        )
        Pagamentos.atualizar(p)
    
    @staticmethod
    def listar_pagamentos():
        return Pagamentos.listar()
    
    @staticmethod
    def buscar_pagamento(id: int):
        return Pagamentos.buscar_por_id(id)
        
    @staticmethod
    def excluir_pagamento(id: int):
        p = Pagamentos.buscar_por_id(id)
        if p is None:
            raise Exception('Pagamento Não encontrado')
        Pagamentos.excluir(id)
