import streamlit as st
from Admin.view import *
from .AlunosUI import AlunosUI
from .MatriculasUI import MatriculasUI
from .PagamentosUI import PagamentosUI
from .TreinoUI import TreinoUI
from .MedidasUI import MedidasUI
from .MusculosUI import MusculosUI
from .PlanosUI import PlanosUI
from .PartCorpoUI import PartCorpoUI
from .CaixaUI import CaixaUI

class IndexUI:
    __logado = False

    @classmethod
    def main(cls):
        st.set_page_config(
            page_title="Academia Iron Man",
            page_icon=":muscle:",
            layout="centered" 
        )
        cls.__logado = True
        if not cls.__logado:
            cls.login()

        if cls.__logado:
            cls.menuAdmin()

    @classmethod
    def login(cls):
        st.title("Login")
        senha = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            if View.validar_login(senha):
                cls.__logado = True
                st.success("Logado com sucesso")
                st.rerun()
            else:
                st.error("Senha inválida")

    @classmethod
    def menuAdmin(cls):


        st.markdown(
            """
            <h1 style='text-align: center;'>
                Academia <strong>Iron Man</strong>
            </h1>
            """,
            unsafe_allow_html=True
        )

        op = st.sidebar.radio('',["Caixa", "Alunos", "Matriculas", "Pagamentos", 'Treinos', 'Medidas', 'Planos', 'Grupos Musculares', 'Fisiologias'])
        if st.sidebar.button('Sair'):
            cls.Logout()


        
        match op.lower():
            case "caixa":
                CaixaUI.main()
            case "alunos":
                AlunosUI.main()
            case 'matriculas':
                MatriculasUI.main()
            case 'pagamentos':
                PagamentosUI.main()
            case 'treinos':
                TreinoUI.main()
            case 'medidas':
                MedidasUI.main()
            case 'planos':
                PlanosUI.main()
            case 'grupos musculares':
                MusculosUI.main()
            case 'fisiologias':
                PartCorpoUI.main()



    @classmethod
    def Logout(cls):
        cls.__logado = False
        st.rerun



