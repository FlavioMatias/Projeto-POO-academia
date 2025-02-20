from Admin.view import *
import streamlit as st
from datetime import datetime

class PagamentosUI:
    @classmethod
    def main(cls):
        src = st.text_input('buscar pagamento')
        with st.expander("Cadastrar Novo Pagamento", expanded=False):
            st.write('a implementar')
        for pagamento in PagamentoView.listar_pagamentos():
            with st.container(border=True):
                aluno = AlunosView.buscar_aluno(pagamento.id_cliente)
                pagamentos, quitar = st.columns((6,1))
                with pagamentos:
                    st.write('ID:', pagamento.id)
                    st.write('aluno:', aluno.nome)
                    st.write('matricula:', pagamento.id_matricula)
                    st.write('emissão:', pagamento.emissao)
                    st.write('Data do pagamento:', pagamento.data_pagamento)
                    st.write('Valor:', pagamento.valor)
                    st.write('Pago:', pagamento.pago)
                    data_vencimento = pagamento.vencimento
                    hoje = datetime.now().date()

                    if data_vencimento < hoje and not pagamento.pago:  
                        st.write('Status: Vencido')
                    else:
                        st.write('Status: Em dia')

                with quitar:
                    if not pagamento.pago:
                        if st.button('Quitar'):
                            PagamentoView.atualizae_pagamento(pagamento.id, pagamento.id_matricula, pagamento.id_cliente, pagamento.emissao.strftime('%d/%m/%Y'), pagamento.vencimento.strftime('%d/%m/%Y'), datetime.now().strftime('%d/%m/%Y'), pagamento.valor, True)
                            st.rerun()
                    else:
                        st.write('Pago')