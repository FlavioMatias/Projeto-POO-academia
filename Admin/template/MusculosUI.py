from Admin.view import *
import streamlit as st

class MusculosUI:
    @classmethod
    def main(cls):
        src = st.text_input('buscar grupo muscular')
        with st.expander("Cadastrar Novo Aluno", expanded=False):
            st.write('a implementar')
            pass

        for musculo in MusculoView.listar_musculos():
            with st.container(border=True):
                treinos, buttons = st.columns((6,1))
                with treinos:
                    st.write(musculo)

                with buttons:
                    if st.button('atualizar'):
                        pass
                    if st.button('exluir'):
                        MusculoView.excluir_musculo(musculo.id)
                        st.rerun()