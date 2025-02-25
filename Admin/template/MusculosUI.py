from Admin.view import *
import streamlit as st

class MusculosUI:
    __page = 'musculos'
    __last_musculo = None

    @classmethod
    def main(cls):
        if cls.__page == 'musculos':
            src = st.text_input('buscar grupo muscular', placeholder="digite o id do grupo muscular")

        if cls.__page == 'musculos':
            with st.container(border=True):
                cls.cadastrar_musculo()

            if not src:
                for musculo in MusculoView.listar_musculos():
                    with st.container(border=True):
                        treinos, buttons = st.columns((6,1))

                        with treinos:
                            st.write('**ID**:', musculo.id)
                            st.write('**Nome**',musculo.nome)

                        with buttons:
                            if st.button('Atualizar', key=f'detalhe{musculo.id}'):
                                cls.__page = 'atualizar'
                                cls.__last_musculo = musculo
                                st.rerun()

                            if st.button('Excluir', key=f'cancelar{musculo.id}'):
                                MusculoView.excluir_musculo(musculo.id)
                                st.rerun()

            else:
                if not MusculoView.buscar_musculo(int(src)):
                    st.info('Musculo nao encontrado')
                else:
                    for musculo in MusculoView.buscar_musculo(int(src)):
                        with st.container(border=True):
                            treinos, buttons = st.columns((6,1))

                            with treinos:
                                st.write(musculo) # fazer embelezamento

                            with buttons:
                                if st.button('Atualizar', key=f'detalhe{musculo.id}'):
                                    cls.__page = 'atualizar'
                                    cls.__last_musculo = musculo
                                    st.rerun()

                                if st.button('Excluir', key=f'cancelar{musculo.id}'):
                                    MusculoView.excluir_musculo(musculo.id)
                                    st.rerun()

        if cls.__page == 'atualizar':
            cls.atualizar_musculo(cls.__last_musculo)

            if st.button('voltar'):
                cls.__page = 'musculos'
                cls.__last_musculo = None
                st.rerun()

    @classmethod
    def cadastrar_musculo(cls):
        with st.expander("Cadastrar Novo Musculo", expanded=False):
            with st.form(key = 'form_cadastro_musculo'):
                nome = st.text_input("Nome:", placeholder="digite o nome do musculo")
                enviar = st.form_submit_button("Cadastrar")

                if enviar:
                    if nome:
                        try:
                            MusculoView.inserir_musculo(nome)
                            st.success("Musculo cadastrado com sucesso")
                        except Exception as e:
                            st.error(e)
                    else:
                        st.error("Preencha todos os campos obrigatórios.")

    @classmethod
    def atualizar_musculo(cls, musculo):
        with st.container(border=True):
            with st.form(key = 'form_cadastro_musculo'):
                nome = st.text_input("Nome:", musculo.nome)
                enviar = st.form_submit_button("Atualizar")

                if enviar:
                    if nome:
                        try:
                            MusculoView.atualizar_musculo(musculo.id, nome)
                            st.success("Musculo atualizado com sucesso")
                        except Exception as e:
                            st.error(e)
                    else:
                        st.error("Preencha todos os campos obrigatórios.")