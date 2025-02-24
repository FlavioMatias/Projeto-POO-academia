import streamlit as st
import pandas as pd
import plotly.express as px
from Admin.view import *

class CaixaUI:
    @staticmethod
    def main():
        st.title("Dashboard de Caixa")
        CaixaUI.status_financeiros()
        CaixaUI.exibir_rendimento_mensal()
        CaixaUI.exibir_rendimento_anual()
        CaixaUI.exibir_caloteiros()

    @staticmethod
    def exibir_rendimento_mensal():
        rendimentos = View.calcular_rendimento_mensal()

        with st.container(border=True):
            st.subheader("Resumo dos Pagamentos do Mês")
            col1, col2 = st.columns(2)
            with st.container(border=True):
                col1.metric("Total Pago", f"R$ {rendimentos['total_pago']:.2f}")
                col2.metric("Total Faltando", f"R$ {rendimentos['total_faltando']:.2f}")

            df_mensal = pd.DataFrame({
                "Situação": ["Pago", "Faltando"],
                "Valor": [rendimentos['total_pago'], rendimentos['total_faltando']]
            })

            fig_mensal = px.bar(
                df_mensal,
                x="Situação",
                y="Valor",
                text="Valor",
                color="Situação",
                color_discrete_map={"Pago": "green", "Faltando": "red"},
                title="Grafico dos Pagamentos",
                labels={"Valor": "Valor (R$)"}
            )
            fig_mensal.update_traces(texttemplate='R$ %{text:.2f}', textposition='outside')
            fig_mensal.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
            with st.container(border=True):
                st.plotly_chart(fig_mensal)

    @staticmethod
    def exibir_rendimento_anual():
        rendimentos_anual = View.calcular_rendimento_anual()
        
        with st.container(border=True):
            st.subheader("Resumo dos Pagamentos do Ano")
            
            # Cálculo da média de lucro anual
            media_lucro_anual = rendimentos_anual['Total Anual']['media_lucro']

            # Criação de colunas para exibir os totais anuais e a média
            cola1, cola2, cola3 = st.columns(3)
            with cola1:
                st.metric("Total Pago", f"R$ {rendimentos_anual['Total Anual']['total_pago']:.2f}")
            with cola2:
                st.metric("Total Faltando", f"R$ {rendimentos_anual['Total Anual']['total_faltando']:.2f}")
            with cola3:
                st.metric("Média de Lucro Anual", f"R$ {media_lucro_anual:.2f}")

            # Criação do DataFrame para os dados mensais (sem a média de lucro)
            df_anual = pd.DataFrame({
                "Mês": list(rendimentos_anual.keys())[:-1],  # Exclui o Total Anual
                "Total Pago": [rendimentos_anual[mês]["total_pago"] for mês in rendimentos_anual if mês != "Total Anual"],
                "Total Faltando": [rendimentos_anual[mês]["total_faltando"] for mês in rendimentos_anual if mês != "Total Anual"]
            })

            # Gráfico de barras para os totais pagos e faltando por mês
            df_melted = df_anual.melt(id_vars="Mês", value_vars=["Total Pago", "Total Faltando"], var_name="Situação", value_name="Valor")
            
            fig_anual = px.bar(
                df_melted,
                x="Mês",
                y="Valor",
                text="Valor",
                color="Situação",
                color_discrete_map={"Total Pago": "green", "Total Faltando": "red"},
                title="Gráfico dos Pagamentos Mensais",
                labels={"Valor": "Valor (R$)"}
            )
            fig_anual.update_traces(texttemplate='R$ %{text:.2f}', textposition='outside')
            fig_anual.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

            with st.container(border=True):
                st.plotly_chart(fig_anual)


    @staticmethod
    def exibir_caloteiros():
        with st.expander('Alunos deventes'):
            for aluno in View.deventes_do_mes():
                matricula = AlunosView.buscar_matricula_aluno(aluno.id)
                if matricula:
                    plano = PlanosView.buscar(matricula.plano)
                with st.container(border=True):
                    st.markdown(f'### {aluno.id} | {aluno.nome}')
                    if matricula:
                        st.text(f'Matricula: {matricula.id}')
                        st.text(f'Plano: {plano.id} | {plano.nome}')
                    else:
                        st.text('Aluno não possui matricula')
    @staticmethod
    def status_financeiros():
        quantidade_pagamentos, nao_pagos = View.pagamentos_do_mes()
        status_do_mes = View.calcular_rendimento_mensal()
        with st.container(border=True):
            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    label="✅ Pagamentos Feitos",
                    value=quantidade_pagamentos,
                    delta_color="normal"
                )

            with col2:
                st.metric(
                    label="❌ Pagamentos Não Feitos",
                    value=nao_pagos,
                    delta_color="inverse"
                )

            st.metric(
                label="💰 Rendimento deste Mês",
                value=f"R$ {status_do_mes['total_pago']:.2f}",
                delta_color="normal"
            )

