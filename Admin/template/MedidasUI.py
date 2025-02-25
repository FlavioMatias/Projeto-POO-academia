from Admin.view import *
import streamlit as st
from datetime import datetime
import time

class MedidasUI:
    __page = 'medidas'
    __last_medicao = None

    @classmethod
    def main(cls):
        if cls.__page == 'medidas':
            src = st.text_input('buscar medição', placeholder="digite o id da medicao")
        
        if cls.__page == 'medidas':
            with st.container(border=True):
                cls.cadastrar_medicao()

            if not src:
                for medição in MedicaoView.listar_medicoes():
                    aluno = AlunosView.buscar_aluno(medição.id_cliente)
                    with st.container(border=True):
                        medidas, detalhe = st.columns((6,1))
                        with medidas:
                            st.write('**Medida do aluno:**', aluno.id, '|', aluno.nome)
                            st.write("**Data:**", medição.data)

                        with detalhe:
                            if st.button('Detalhes', key=f'detalhe{medição.id}'):
                                cls.__page = 'detalhes'
                                cls.__last_medicao = medição
                                st.rerun()

                            if st.button('Exluir', key=f'cancelar{medição.id}'):
                                MedicaoView.excluir_medicao(medição.id)
                                st.rerun()

            else:
                if not MedicaoView.buscar_medicao(int(src)):
                    st.info('Medicao nao encontrada')
                else:
                    for medição in MedicaoView.listar_medicoes():
                        with st.container(border=True):
                            medidas, detalhe = st.columns((6,1))
                            with medidas:
                                st.write(medição) 

                            with detalhe:
                                if st.button('Detalhes', key=f'detalhe{medição.id}'):
                                    cls.__page = 'detalhes'
                                    cls.__last_medicao = medição
                                    st.rerun()

                                if st.button('Exluir', key=f'cancelar{medição.id}'):
                                    MedicaoView.excluir_medicao(medição.id)
                                    st.rerun()

        if cls.__page == 'detalhes':
            cls.detalhes_medicao(cls.__last_medicao)

            if st.button('voltar'):
                cls.__page = 'medidas'
                cls.__last_medicao = None
                st.rerun()

    @classmethod
    def detalhes_medicao(cls, medicao):
        aluno = AlunosView.buscar_aluno(medicao.id_cliente)

        with st.container(border=True):
            st.subheader("Detalhes da Medição")
            st.write(f"**Medição do aluno:** {aluno.nome}")
            st.write(f"**Data da Medição:** {medicao.data}")

        with st.container(border=True):
            st.subheader("Medidas do Aluno")
            with st.container(border=True):
                cls.cadastrar_medida()

            medidas = MedidaView.listar_medidas_do_aluno(medicao.id)
            if medidas:
                for medida in medidas:
                    with st.container(border=True):
                        medidas, detalhe = st.columns((6,1))
                        with medidas:
                            partecorpo = PartCorpoView.buscar_parte_corpo(medida.id_partcorpo)
                            if partecorpo:
                                st.write(f"**Parte do Corpo:** {partecorpo.nome}")
                                st.write(f"**Valor:** {medida.valor} {partecorpo.unidade}")
                            else:
                                st.info('Parte do Corpo nao encontrada')

                        with detalhe:
                            if st.button('Excluir', key=f'cancelar{medida.id}'):
                                MedidaView.excluir_medida(medida.id)
                                st.rerun()
            else:
                st.info('Nenhuma medida cadastrada')

    @classmethod
    def cadastrar_medicao(cls):
        id_alunos = [f"{aluno.id} | {aluno.nome}" for aluno in AlunosView.listar_alunos()]
        id_aluno_selecionado = None

        with st.expander("Cadastrar medicao", expanded=False):
            aluno_selecionado = st.selectbox('Escolha o aluno', id_alunos)

            if aluno_selecionado:
                id_aluno_selecionado = int(aluno_selecionado.split(" | ")[0])
            else:
                st.info('Nenhum aluno para cadastrar medicao')

            if st.button("cadastrar"):
                if id_aluno_selecionado:
                    MedicaoView.inserir_medicao(id_aluno_selecionado)
                    st.success("Medicao cadastrada com sucesso")
                else:
                    st.error('Selecione um aluno')  

    @classmethod
    def cadastrar_medida(cls):
        id_partcorpo = [f"{partecorpo.id} | {partecorpo.nome}" for partecorpo in PartCorpoView.listar_partescorpo()]
        id_partcorpo_selecionado = None

        with st.expander("cadastrar medida", expanded=False):
            partecorpo_selecionado = st.selectbox('Escolha a parte do corpo', id_partcorpo)

            if partecorpo_selecionado:
                id_partcorpo_selecionado = int(partecorpo_selecionado.split(" | ")[0])
                valor = st.number_input('Digite o valor', min_value=0.0, step=0.1)
            else:
                st.info('Nenhum partecorpo para cadastrar medida')

            if st.button("cadastrar"):
                if id_partcorpo_selecionado:
                    MedidaView.inserir_medida(cls.__last_medicao.id,id_partcorpo_selecionado, valor)
                    st.success("Medida cadastrada com sucesso")
                else:
                    st.error('Selecione uma parte do corpo')