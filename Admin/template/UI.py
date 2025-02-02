from Admin.view.adm_view import View 
import streamlit as st
from datetime import datetime
class UI:
    def main():
        st.title("Gestão de Alunos")

        # Menu lateral para navegação
        menu = st.sidebar.selectbox("Menu", ["Inserir Aluno", "Listar Alunos"])

        if menu == "Inserir Aluno":
            st.header("Inserir Novo Aluno")
            # Campos para inserir dados do aluno
            nome = st.text_input("Nome")
            email = st.text_input("Email")
            tel = st.text_input("Telefone")
            data_cadastro = st.text_input("Data de Cadastro (ex: 01/02/2025)", value=datetime.today().strftime('%d/%m/%Y'))
            nascimento = st.text_input("Data de Nascimento (ex: 15/08/1990)")
            sexo = st.selectbox("Sexo", ["M", "F", "Outro"])
            cpf = st.text_input("CPF")
            rg = st.text_input("RG")
            profissao = st.text_input("Profissão")

            # Botão para inserir o aluno
            if st.button("Inserir Aluno"):
                try:
                    View.inserir_aluno(nome, email, tel, data_cadastro, nascimento, sexo, cpf, rg, profissao)
                    st.success("Aluno inserido com sucesso!")
                except Exception as e:
                    st.error(f"Ocorreu um erro: {e}")

        elif menu == "Listar Alunos":
            st.header("Lista de Alunos")
            alunos = View.listar_alunos()
            if alunos:
                # Exibe cada aluno com seus atributos
                for aluno in alunos:
                    st.write(aluno.to_dict())
                    st.markdown("---")
            else:
                st.write("Nenhum aluno cadastrado.")
