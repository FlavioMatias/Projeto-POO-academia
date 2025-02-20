from Admin.view import *
import streamlit as st

class PartCorpoUI:
    @classmethod
    def main(cls):
        src = st.text_input('buscar parte do corpo')
        with st.expander("Cadastrar Parte do Corpo", expanded=False):
            st.write('a implementar')
            pass
        
        for parte_corpo in PartCorpoView.listar_partescorpo():
            with st.container(border=True):
                pc, detalhe = st.columns((6,1))
                with pc:
                    st.write(parte_corpo)
                with detalhe:
                    if st.button('atualizar'):
                        pass
                    if st.button('exluir'):
                        PartCorpoView.excluir_parte_corpo(parte_corpo.id)
                        st.rerun()
