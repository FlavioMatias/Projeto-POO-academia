from Admin.view import *
import streamlit as st

class PartCorpoUI:
    __page = 'partescorpo'
    __last_parte_corpo = None

    @classmethod
    def main(cls):
        if cls.__page == 'partescorpo':
            src = st.text_input('buscar parte do corpo', placeholder="digite o id da parte do corpo")
        
        if cls.__page == 'partescorpo':
            with st.container(border=True):
                cls.cadastrar_parte_corpo()

            if not src:
                for parte_corpo in PartCorpoView.listar_partescorpo():
                    with st.container(border=True):
                        pc, detalhe = st.columns((6,1))
                        
                        with pc:
                            st.write(parte_corpo) # necessario fazer embelezamento
                        
                        with detalhe:
                            if st.button('Atualizar', key=f'detalhe{parte_corpo.id}'):
                                cls.__page = 'atualizar'
                                cls.__last_parte_corpo = parte_corpo
                                st.rerun()
                            
                            if st.button('Excluir', key=f'cancelar{parte_corpo.id}'):
                                PartCorpoView.excluir_parte_corpo(parte_corpo.id)
                                st.rerun()  

            else:
                if not PartCorpoView.buscar_parte_corpo(int(src)):
                    st.info('Parte do Corpo nao encontrado')
                else:
                    for parte_corpo in PartCorpoView.buscar_parte_corpo(int(src)):
                        with st.container(border=True):
                            pc, detalhe = st.columns((6,1))
                            
                            with pc:
                                st.write(parte_corpo) # necessario fazer embelezamento
                            
                            with detalhe:
                                if st.button('Atualizar', key=f'detalhe{parte_corpo.id}'):
                                    cls.__page = 'atualizar'
                                    cls.__last_parte_corpo = parte_corpo
                                    st.rerun()
                                
                                if st.button('Excluir', key=f'cancelar{parte_corpo.id}'):
                                    PartCorpoView.excluir_parte_corpo(parte_corpo.id)
                                    st.rerun()

        if cls.__page == 'atualizar':
            cls.atualizar_parte_corpo(cls.__last_parte_corpo)

            if st.button('voltar'):
                cls.__page = 'partescorpo'
                cls.__last_parte_corpo = None
                st.rerun()

    @classmethod
    def cadastrar_parte_corpo(cls):
        with st.expander("Cadastrar Parte do Corpo", expanded=False):
            with st.form(key = 'form_cadastro_parte_corpo'):
                nome = st.text_input("Nome:")
                unidade = st.text_input("Unidade:")

                enviar = st.form_submit_button("Cadastrar")

                if enviar:
                    if nome and unidade:
                        try:
                            PartCorpoView.inserir_parte_corpo(nome, unidade)
                            st.success("Parte do Corpo cadastrada com sucesso")
                        except Exception as e:
                            st.error(e)
                    else:
                        st.error("Preencha todos os campos obrigatórios.")

    @classmethod
    def atualizar_parte_corpo(cls, parte_corpo):
        with st.container(border=True):
            with st.form(key = 'form_cadastro_parte_corpo'):
                nome = st.text_input("Nome:", parte_corpo.nome)
                unidade = st.text_input("Unidade:", parte_corpo.unidade)

                enviar = st.form_submit_button("Atualizar")

                if enviar:
                    if nome and unidade:
                        PartCorpoView.atualizar_partcorpo(parte_corpo.id, nome, unidade)
                        st.success("Parte do Corpo atualizada com sucesso")
                    else:
                        st.error("Preencha todos os campos obrigatórios.")