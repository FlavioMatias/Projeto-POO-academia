import streamlit as st
from Admin.view import *

logado = False

class IndexUI:
    @staticmethod
    def main():
        global logado
        if not logado:
            IndexUI.login()

        if logado:
            IndexUI.menuAdmin()

    def login():
        global logado
        st.title("Login")
        senha = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            if View.validar_login(senha):
                logado = True
                st.success("Logado com sucesso")
                st.rerun()

                
            else:
                st.error("Senha inválida")
        
    def menuAdmin():
        st.title("academia iron man")
        st.subheader("Menu Admin")
        st.sidebar.selectbox("Opções", ["Cadastrar", "Listar", "Deletar"])



