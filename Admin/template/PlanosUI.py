from Admin.view import *
import streamlit as st

class PlanosUI:
    @classmethod
    def main(cls):
        src = st.text_input('buscar plano')
        with st.expander("Cadastrar Novo Plano", expanded=False):
            st.write('a implementar')
            pass

        for plano in PlanosView.listar_planos():
            with st.container(border=True):
                p, buttons = st.columns((6,1))
                with p:
                    st.write(plano)

                with buttons:
                    if st.button('atualizar', key=f'aplano-{plano.id}'):
                        pass
                    if st.button('exluir', key=f'eplano-{plano.id}'):
                        PlanosView.excluir_plano(plano.id)
                        st.rerun()