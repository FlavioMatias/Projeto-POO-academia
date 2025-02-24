from Admin.view import *
import streamlit as st
from datetime import datetime
from time import sleep

class PagamentosUI:
    @classmethod
    def main(cls):

        src = st.text_input('buscar pagamentos', placeholder='id matricula')
        with st.expander("Cadastrar Novo Pagamento", expanded=False):
            cls.cadastra_pagamento()
        if not src:
            for pagamento in PagamentoView.listar_pagamentos():
                with st.container(border=True):
                    aluno = AlunosView.buscar_aluno(pagamento.id_cliente)
                    pagamentos, quitar = st.columns((6,1))
                    try:
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
                    except:
                        st.error('pagamento com erro')
                with quitar:
                    if not pagamento.pago:
                        if st.button('Quitar', key=f'quitar{pagamento.id}'):
                            PagamentoView.atualizae_pagamento(pagamento.id, pagamento.id_matricula, pagamento.id_cliente, pagamento.emissao.strftime('%d/%m/%Y'), pagamento.vencimento.strftime('%d/%m/%Y'), datetime.now().strftime('%d/%m/%Y'), pagamento.valor, True)
                            st.rerun()
                    else:
                        st.write('Pago')

        else:
            pagamentos_filtrados = list(filter(lambda pagamento: pagamento.id_matricula == int(src), PagamentoView.listar_pagamentos()))
            for pagamento in pagamentos_filtrados:
                with st.container(border=True):
                    aluno = AlunosView.buscar_aluno(pagamento.id_cliente)
                    pagamentos, quitar = st.columns((6,1))
                    try:
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
                    except:
                        st.error('pagamento com erro')
                with quitar:
                    if not pagamento.pago:
                        if st.button('Quitar', key=f'quitar{pagamento.id}'):
                            PagamentoView.atualizae_pagamento(pagamento.id, pagamento.id_matricula, pagamento.id_cliente, pagamento.emissao.strftime('%d/%m/%Y'), pagamento.vencimento.strftime('%d/%m/%Y'), datetime.now().strftime('%d/%m/%Y'), pagamento.valor, True)
                            st.rerun()
                    else:
                        st.write('Pago')


    @classmethod        
    def cadastra_pagamento(cls):
        with st.container(border=True):
            matriculas = MatriculaView.listar_matriculas()
            opcoes_matricula = {f"{matricula.id} - {AlunosView.buscar_aluno(matricula.id_aluno).nome}": matricula for matricula in matriculas if matricula.ativa}
            escolha = st.selectbox("Matrícula", list(opcoes_matricula.keys()))
            matricula_selecionada = opcoes_matricula[escolha]
            validade = st.date_input("Data de Validade", value=datetime.today().date(), format='DD/MM/YYYY')
            if st.button('adcionar pagamento'):
                try:
                    PagamentoView.inserir_pagamento(id_matricula=matricula_selecionada.id,id_cliente=matricula_selecionada.id_aluno, validade=validade.strftime("%d/%m/%Y"))
                except Exception as e:
                    st.error('Erro:', e)
                else:
                    st.success('pagamento gerado')
                sleep(2)
                st.rerun()