from .PagamentoView import PagamentoView
from .AlunosView import AlunosView
from .MatriculaView import MatriculaView
from .PlanosView import PlanosView

from datetime import datetime

class View:
    @staticmethod
    def validar_login(senha):
        if senha == 'admin':
            return True
        return False
    
    def renovar_matricula():
        pass
    def matricular_aluno(id_aluno, id_plano):
        try:
            MatriculaView.inserir_matricula(id_aluno, id_plano, datetime.today().strftime('%d/%m/%Y'))
            plano = PlanosView.buscar(id_plano)
            for matricula in MatriculaView.listar_matriculas():
                if matricula.id_aluno == id_aluno and matricula.plano == id_plano and matricula.ativa:
                    matric = matricula
                    break

            for time in range(1, int(plano.tempo.split()[0])):
                PagamentoView.inserir_pagamento(matric.id, matric.id_aluno,validade=None, intervalo_meses=time)
        except Exception as e:
            raise ValueError(f'nao foi possivel realizar a matricula por: {e}')
 
    def calcular_rendimento_mensal():
        valor_total: float = 0.0
        valor_faltando: float = 0.0
        hoje = datetime.today()

        for pagamento in PagamentoView.listar_pagamentos():
            vencimento = pagamento.vencimento
   
            if vencimento.year == hoje.year and vencimento.month == hoje.month:
                if pagamento.pago:
                    valor_total += pagamento.valor
                else:
                    valor_faltando += pagamento.valor

        return {"total_pago": valor_total, "total_faltando": valor_faltando}
    
    def calcular_rendimento_anual():
        rendimentos_por_mes = {month: {"total_pago": 0.0, "total_faltando": 0.0} for month in [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]}

        total_pago_ano = 0.0
        total_faltando_ano = 0.0
        total_pagamentos_ano = 0

        hoje = datetime.today()

        for pagamento in PagamentoView.listar_pagamentos():
            vencimento = pagamento.vencimento 
            if vencimento.year == hoje.year:
                mes = vencimento.month - 1  # Para pegar o índice correto do mês
                if pagamento.pago:
                    rendimentos_por_mes[list(rendimentos_por_mes.keys())[mes]]["total_pago"] += pagamento.valor
                    total_pago_ano += pagamento.valor
                    total_pagamentos_ano += 1
                else:
                    rendimentos_por_mes[list(rendimentos_por_mes.keys())[mes]]["total_faltando"] += pagamento.valor
                    total_faltando_ano += pagamento.valor

        # Cálculo da média de lucro anual
        media_lucro_anual = total_pago_ano / total_pagamentos_ano if total_pagamentos_ano > 0 else 0.0

        # Adiciona os totais anuais e a média ao dicionário
        rendimentos_por_mes["Total Anual"] = {
            "total_pago": total_pago_ano,
            "total_faltando": total_faltando_ano,
            "media_lucro": media_lucro_anual
        }

        return rendimentos_por_mes
    
    def deventes_do_mes():
        hoje = datetime.today().date()
        ids_clientes_vencidos = set()  

        for pagamento in PagamentoView.listar_pagamentos():
            vencimento = pagamento.vencimento

            if vencimento < hoje and not pagamento.pago:
                ids_clientes_vencidos.add(pagamento.id_cliente)

        ids_clientes_vencidos = list(ids_clientes_vencidos)
        caloteiros = []
        for alunos in AlunosView.listar_alunos():
            if alunos.id in ids_clientes_vencidos:
                caloteiros.append(alunos)
        return caloteiros
    
    def pagamentos_do_mes():
        quantidade = 0
        nao_pagos =  0
        for pagamento in PagamentoView.listar_pagamentos():
            vencimento = pagamento.vencimento
            hoje = datetime.today()
            if vencimento.year == hoje.year and vencimento.month == hoje.month and  pagamento.pago:
                quantidade += 1
            elif vencimento.year == hoje.year and vencimento.month == hoje.month and not pagamento.pago:
                nao_pagos += 1

        return quantidade, nao_pagos
    
    def renovar_treino():
        pass
    def renovar_medicao():
        pass