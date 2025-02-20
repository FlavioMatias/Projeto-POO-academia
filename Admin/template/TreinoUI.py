from Admin.view import *
import streamlit as st

class TreinoUI:
    @classmethod
    def main(cls):
        src = st.text_input('buscar treino')
        for treino in TreinoAlunoView.listar_treinos():
            with st.container(border=True):
                aluno = AlunosView.buscar_aluno(treino.id_aluno)
                treinos, detalhe = st.columns((6,1))
                with treinos:
                    st.write('ID:', treino.id)
                    st.write('aluno:', aluno.nome)
                    st.write('Data:', treino.data)
                    st.write('Atividades:', treino.atv)

                with detalhe:
                    if st.button('datalhes', key=treino.id):
                        cls.detalhes_treino(treino.id)
                        st.rerun()
                    if st.button('exluir', key=treino.id):
                        TreinoAlunoView.excluir_treinoAluno(treino.id)
                        st.rerun()
    @classmethod
    def detalhes_treino(cls, id_treino):
        treinos_do_treinoaluno = []
        for treino in TreinoView.listar_treinos():
            if treino.id_treino == id_treino:
                treinos_do_treinoaluno.append(treino)
        for trein in treinos_do_treinoaluno:
            with st.container(border=True):
                st.write(trein.descricao)
