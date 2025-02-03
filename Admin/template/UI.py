from Admin.view.adm_view import View 
import streamlit as st
from datetime import datetime
class UI:
    def main():
        st.title("Gestão de Alunos")

        menu = st.sidebar.selectbox("Menu", ["Inserir Aluno", "Listar Alunos"])

        if menu == "Inserir Aluno":
            st.header("Inserir Novo Aluno")

            nome = st.text_input("Nome")
            email = st.text_input("Email")
            tel = st.text_input("Telefone")
            data_cadastro = st.text_input("Data de Cadastro", value=datetime.today().strftime('%d/%m/%Y'))
            nascimento = st.text_input("Data de Nascimento")
            sexo = st.selectbox("Sexo", ["M", "F", "Outro"])
            cpf = st.text_input("CPF")
            rg = st.text_input("RG")
            profissao = st.text_input("Profissão")
            bairro = st.text_input("bairro")
            cep = st.text_input("cep")
            rua = st.text_input("rua")
            numero = st.text_input("numero da casa")

            if st.button("Inserir Aluno"):
                try:
                    View.inserir_aluno(nome, email, tel, data_cadastro, nascimento, sexo, cpf, rg, profissao, bairro, cep, rua, numero)
                    st.success("Aluno inserido com sucesso!")

                except Exception as e:
                    st.error(f"Ocorreu um erro: {e}")

        elif menu == "Listar Alunos":
            st.header("Lista de Alunos")
            alunos = View.listar_alunos()
            endereços = View.listar_endereços()
            print(endereços)
            if alunos:
                for aluno in alunos:
                    with st.container(border=True):
                        st.write(f"ID: {aluno.id}")
                        st.write(f"Nome: {aluno.nome}")
                        st.write(f"Email: {aluno.email}")
                        st.write(f"Telefone: {aluno.tel}")
                        st.write(f"Data de Cadastro: {aluno.data_cadastro}")
                        st.write(f"Data de Nascimento: {aluno.nascimento}")
                        st.write(f"Sexo: {aluno.sexo}")
                        st.write(f"CPF: {aluno.cpf}")
                        st.write(f"RG: {aluno.rg}")
                        st.write(f"Profissão: {aluno.profissao}")

                        endereços_aluno = [endereco for endereco in endereços if endereco.id_cliente == aluno.id]
                        
                        if endereços_aluno:
                            for endereco in endereços_aluno:
                                with st.container(border=True):
                                    st.subheader('Endereço')
                                    st.write(f"ID do Endereço: {endereco.id}")
                                    st.write(f"ID do Cliente: {endereco.id_cliente}")
                                    st.write(f"Bairro: {endereco.bairro}")
                                    st.write(f"CEP: {endereco.cep}")
                                    st.write(f"Rua: {endereco.rua}")
                                    st.write(f"Número: {endereco.numero}")
                        else:
                            with st.container(border=True):
                                st.write('Não consta endereço para este aluno')


            else:
                st.write("Nenhum aluno cadastrado.")
