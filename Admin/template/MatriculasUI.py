from Admin.view import *
import streamlit as st


class MatriculasUI:
    __page = 'matriculas'
    __last_matricula = None

    @classmethod
    def main(cls):
        src = st.text_input('buscar matricula')
        
        if cls.__page == 'matriculas':
            with st.container(border=True):
                cls.matricular_aluno()
            for matricula in MatriculaView.listar_matriculas():
                with st.container(border=True):
                    dados, detalhe = st.columns((6,1))
                    with dados:
                        st.write('ID da matricula:', matricula.id)
                        st.write('ID do aluno:', matricula.id_aluno)
                        st.write('ID do plano:', matricula.plano)
                        st.write('Data da matricula:', matricula.data)

                    with detalhe:
                        if st.button('datalhes'):
                            cls.__page = 'detalhes'
                            cls.__last_matricula = matricula
                            st.rerun()
                        if st.button('Cancelar'):
                            MatriculaView.atualizar_matricula(matricula.id, matricula.id_aluno, matricula.plano, matricula.data, matricula.validade, False)
                            st.rerun()

        if cls.__page == 'detalhes':
            cls.detalhes_matricula(cls.__last_matricula.id)
            if st.button('voltar'):
                cls.__page = 'matriculas'
                cls.__last_matricula = None
                st.rerun()
            if st.button('atualizar'):
                pass
            if st.button('renovar'):
                pass

    @classmethod
    def detalhes_matricula(cls, id_matricula):
        matricula = MatriculaView.buscar_matricula(id_matricula)
        aluno = AlunosView.buscar_aluno(matricula.id_aluno)
        plano = PlanosView.buscar(matricula.plano)
        
        with st.container(border=True):
            st.write(matricula)
            st.write(aluno)
            st.write(plano)

    @classmethod
    def matricular_aluno(cls):
        with st.expander("matricular aluno", expanded=False):
            st.write('a implementar')
            pass