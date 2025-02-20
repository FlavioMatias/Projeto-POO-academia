from Admin.view import *
import streamlit as st

class MedidasUI:
    @classmethod
    def main(cls):
        src = st.text_input('buscar medição')
        
        for medição in MedicaoView.listar_medicoes():
            with st.container(border=True):
                aluno = AlunosView.buscar_aluno(medição.id_cliente)
                medidas, detalhe = st.columns((6,1))
                with medidas:
                    st.write(medição)
                with detalhe:
                    if st.button('datalhes'):
                        cls.detalhes_medicao(medição.id)
                        st.rerun()
                    if st.button('exluir'):
                        MedicaoView.excluir_medicao(medição.id)
                        st.rerun()
    @classmethod
    def detalhes_medicao(cls, id_medicao):
        medidas_da_medição = []
        for medida in MedidaView.listar_medidas():
            if medida.id_medicao == id_medicao:
                medidas_da_medição.append(medida)
        for med in medidas_da_medição:
            with st.container(border=True):
                st.write(med)