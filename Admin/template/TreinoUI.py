from Admin.view import *
import streamlit as st

class TreinoUI:
    __page = 'treinos'
    __last_treino = None

    @classmethod
    def main(cls):
        if cls.__page == 'treinos':
            src = st.text_input('buscar treino')

        if cls.__page == 'treinos':
            with st.container(border=True):
                cls.cadastrar_treino()

            if not src:
                for treino in TreinoAlunoView.listar_treinos():
                    with st.container(border=True):
                        aluno = AlunosView.buscar_aluno(treino.id_aluno)
                        treinos, detalhe = st.columns((6,1))
                        with treinos:
                            st.write(treino)

                        with detalhe:
                            if st.button('Detalhes', key=f"detalhe{treino.id}"):
                                cls.__page = 'detalhes'
                                cls.__last_treino = treino
                                st.rerun()
                            if st.button('Excluir', key=f"cancelar{treino.id}"):
                                TreinoAlunoView.excluir_treinoAluno(treino.id)
                                st.rerun()

            else:
                for treino in TreinoAlunoView.buscar_treino(int(src)):
                    with st.container(border=True):
                        aluno = AlunosView.buscar_aluno(treino.id_aluno)
                        treinos, detalhe = st.columns((6,1))
                        with treinos:
                            st.write(treino)

                        with detalhe:
                            if st.button('Detalhes', key=f"detalhe{treino.id}"):
                                cls.__page = 'detalhes'
                                cls.__last_treino = treino
                                st.rerun()
                            if st.button('Excluir', key=f"cancelar{treino.id}"):
                                TreinoAlunoView.excluir_treinoAluno(treino.id)
                                st.rerun()

        if cls.__page == 'detalhes':
            cls.detalhes_treino(cls.__last_treino)

            if st.button('voltar'):
                cls.__page = 'treinos'
                cls.__last_treino = None
                st.rerun()

    @classmethod
    def detalhes_treino(cls, treino):
        aluno = AlunosView.buscar_aluno(treino.id_aluno)

        with st.container(border=True):
            st.subheader("Detalhes do Treino")
            st.write(f"**Treino do aluno:** {aluno.nome}")
            st.write(f"**Data do Treino:** {treino.data}")

        with st.container(border=True):
            st.subheader("Exercícios do Treino")
            with st.container(border=True):
                cls.cadastrar_exercicio()

            exercicios = TreinoView.listar_treino_do_treinoaluno(treino.id)
            if exercicios:
                for exercicio in exercicios:
                    with st.container(border=True):
                        exercicios, detalhe = st.columns((6,1))
                        with exercicios:
                            exercicio = TreinoView.buscar_treino(exercicio.id_musculo)
                            st.write(exercicio)
                        with detalhe:
                            if st.button('Excluir', key=f"cancelar{exercicio.id}"):
                                TreinoView.excluir_treino(exercicio.id)
                                st.rerun()

    @classmethod
    def cadastrar_treino(cls):
        id_alunos = [f"{aluno.id} | {aluno.nome}" for aluno in AlunosView.listar_alunos()]
        id_aluno_selecionado = None

        with st.expander("Cadastrar treino", expanded=False):
            aluno_selecionado = st.selectbox('Escolha o aluno', id_alunos)

            if aluno_selecionado:
                id_aluno_selecionado = int(aluno_selecionado.split(" | ")[0])
            else:
                st.info('Nenhum aluno para cadastrar treino')

            if st.button("cadastrar"):
                if id_aluno_selecionado:
                    TreinoAlunoView.inserir_treinoAluno(id_aluno_selecionado)
                    st.success("Treino cadastrado com sucesso")
                else:
                    st.error('Selecione um aluno')


    @classmethod
    def cadastrar_exercicio(cls):
        id_exercicios = [f"{exercicio.id} | {exercicio.nome}" for exercicio in MusculoView.listar_musculos()]
        id_exercicio_selecionado = None

        with st.expander("Cadastrar exercicio", expanded=False):
            exercicio_selecionado = st.selectbox('Escolha o musculo', id_exercicios)

            if exercicio_selecionado:
                id_exercicio_selecionado = int(exercicio_selecionado.split(" | ")[0])
                descricao = st.text_input('Descrição', value="")
            else:
                st.info('Nenhum exercicio para cadastrar treino')

            if st.button("cadastrar"):
                if id_exercicio_selecionado:
                    TreinoView.inserir_treino(id_exercicio_selecionado, cls.__last_treino.id, descricao)
                    st.success("Exercicio cadastrado com sucesso")
                else:
                    st.error('Selecione um exercicio')