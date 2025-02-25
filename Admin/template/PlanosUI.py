from Admin.view import *
import streamlit as st

class PlanosUI:
    __page = 'planos'
    __last_plano = None

    @classmethod
    def main(cls):
        if cls.__page == 'planos':
            src = st.text_input('buscar plano', placeholder="digite o id do plano")
        
        if cls.__page == 'planos':
            with st.container(border=True):
                cls.cadastrar_plano()

            if not src:
                for plano in PlanosView.listar_planos():
                    with st.container(border=True):
                        p, buttons = st.columns((6,1))

                        with p:
                            st.write(plano) # necessario fazer embelezamento

                        with buttons:
                            if st.button('Atualizar', key=f'aplano-{plano.id}'):
                                cls.__page = 'atualizar'
                                cls.__last_plano = plano
                                st.rerun()

                            if st.button('Excluir', key=f'eplano-{plano.id}'):
                                PlanosView.excluir_plano(plano.id)
                                st.rerun()

            else:
                if not PlanosView.buscar_plano(int(src)):
                    st.info('Plano nao encontrado')
                else:
                    for plano in PlanosView.buscar_plano(int(src)):
                        with st.container(border=True):
                            p, buttons = st.columns((6,1))

                            with p:
                                st.write(plano) # necessario fazer embelezamento

                            with buttons:
                                if st.button('Atualizar', key=f'aplano-{plano.id}'):
                                    cls.__page = 'atualizar'
                                    cls.__last_plano = plano
                                    st.rerun()

                                if st.button('Excluir', key=f'eplano-{plano.id}'):
                                    PlanosView.excluir_plano(plano.id)
                                    st.rerun()

        if cls.__page == 'atualizar':
            cls.atualizar_plano(cls.__last_plano)

            if st.button('voltar'):
                cls.__page = 'planos'
                cls.__last_plano = None
                st.rerun()

    @classmethod
    def cadastrar_plano(cls):
        with st.expander("Cadastrar Novo Plano", expanded=False):
            with st.form(key = 'form_cadastro_plano'):
                nome = st.text_input("Nome:", placeholder="digite o nome do plano")
                valor = st.text_input("Valor:", placeholder="digite o valor do plano")
                tempo = st.text_input("Tempo:", placeholder="digite o tempo do plano")

                enviar = st.form_submit_button("Cadastrar")

                if enviar:
                    if nome and valor and tempo:
                        try:
                            PlanosView.inserir_plano(nome, float(valor), tempo)
                            st.success("Plano cadastrado com sucesso")
                        except Exception as e:
                            st.error(e)
                    else:
                        st.error("Preencha todos os campos obrigatórios.")

    @classmethod
    def atualizar_plano(cls, plano):
        with st.container(border=True):
            with st.form(key = 'form_cadastro_plano'):
                nome = st.text_input("Nome:", plano.nome)
                valor = st.text_input("Valor:", plano.valor)
                tempo = st.text_input("Tempo:", plano.tempo)

                enviar = st.form_submit_button("Atualizar")

                if enviar:
                    if nome and valor and tempo:
                        PlanosView.atualizar_plano(plano.id, nome, float(valor), tempo)
                        st.success("Plano atualizado com sucesso")
                    else:
                        st.error("Preencha todos os campos obrigatórios.")