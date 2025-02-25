import streamlit as st
from Admin.view import *
from datetime import datetime

class AlunosUI:
    __page = 'alunos'
    __last_aluno = None

    @classmethod
    def main(cls):
        if cls.__page == 'alunos':
            src = st.text_input('buscar Aluno')
            with st.container(border=True):
                cls.cadastrar_aluno()
            for aluno in AlunosView.listar_alunos():
                with st.container(border=True):
                    dados, buttons = st.columns((6,1))
                    with dados:
                        st.write('ID do aluno:', aluno.id)
                        st.write('Nome:', aluno.nome)
                        st.write('Cadastrado em:', aluno.data_cadastro)
                    with buttons:
                        if st.button('datalhes'):
                            cls.__page = 'detalhes'
                            cls.__last_aluno = aluno
                            st.rerun()
                        if st.button('exluir'):
                            AlunosView.excluir_aluno(aluno.id)
                            st.rerun()

        

        if cls.__page == 'detalhes':
            cls.detalhes_aluno(cls.__last_aluno.id)
            if st.button('atualizar'):
                pass #cls.atualizar_aluno(cls.__last_aluno.id)

            if st.button('adcionar treino'):
                pass
            if st.button('adcionar medição'):
                pass

            if st.button('matricular'):
                pass

            if st.button('voltar'):
                cls.__page = 'alunos'
                cls.__last_aluno = None
                st.rerun()
            
    
    @classmethod
    def detalhes_aluno(cls, id_aluno):
        aluno, endereço = AlunosView.buscar_aluno(id_aluno), AlunosView.buscar_endereco_aluno(id_aluno)
        matricula = AlunosView.buscar_matricula_aluno(id_aluno)

        with st.container(border=True):
            st.write(aluno)
            st.write(endereço)
            st.write(matricula)

        


    @classmethod
    def cadastrar_aluno(cls):

        with st.expander("Cadastrar Novo Aluno", expanded=False): 
            with st.form(key='form_cadastro_aluno'):
                nome = st.text_input("Nome Completo:")
                cpf = st.text_input("CPF:")
                email = st.text_input("E-mail:")
                senha = st.text_input("Senha:", type="password")
                tel = st.text_input("Telefone:")
                datacad = st.date_input("Data de Cadastro:",format="DD/MM/YYYY", value=datetime.now().date())
                datanascimento = st.date_input("Data de Nascimento:", format="DD/MM/YYYY")
                sexo = st.selectbox("Sexo:", ["M", "F", "Outro"])
                rg = st.text_input("RG:")
                profissao = st.text_input("Profissão:")
                st.write('Endereço:')
                bairro = st.text_input("Bairro:")
                cep = st.text_input("CEP:")
                rua = st.text_input("Rua:")
                num = st.text_input("Número:")

                enviar = st.form_submit_button("Cadastrar")

                if enviar:
                    if nome and cpf and email:
                        AlunosView.inserir_aluno(nome, cpf, email, senha, tel, datacad, datanascimento, sexo, rg, profissao, bairro, cep, rua, num)
                    else:
                        st.error("Preencha todos os campos obrigatórios.")
    @classmethod
    def atualizar_aluno(cls, id_aluno):
        aluno, endereço = AlunosView.buscar_aluno(id_aluno), AlunosView.buscar_endereco_aluno(id_aluno)
        matricula = AlunosView.buscar_matricula_aluno(id_aluno)
        
        with st.container(border=True):
            with st.form(key='form_atualizar_aluno'):
                id = st.number_input("ID Aluno", value=aluno.id, step=1)
                nome = st.text_input("Nome Completo:", value=aluno.nome)
                cpf = st.text_input("CPF:", value=aluno.cpf)
                email = st.text_input("E-mail:", value=aluno.email)
                senha = st.text_input("Senha:", type="password", value=aluno.senha)
                tel = st.text_input("Telefone:", value=aluno.tel)
                datacad = st.date_input("Data de Cadastro:", format="DD/MM/YYYY", value=datetime.strptime(aluno.data_cadastro, "%d/%m/%Y").date())
                datanascimento = st.date_input("Data de Nascimento:", format="DD/MM/YYYY", value=aluno.nascimento)
                sexo = st.selectbox("Sexo:", ["M", "F", "Outro"], index=["M", "F", "Outro"].index(aluno.sexo))
                rg = st.text_input("RG:", value=aluno.rg)
                profissao = st.text_input("Profissão:", value=aluno.profissao)

                st.write('Endereço:')
                bairro = st.text_input("Bairro:", value=endereço.bairro)
                cep = st.text_input("CEP:", value=endereço.cep)
                rua = st.text_input("Rua:", value=endereço.rua)
                num = st.text_input("Número:", value=endereço.numero)

                submeter = st.form_submit_button("Atualizar")

                if submeter:
                    if nome and cpf and email:
                        AlunosView.Atualizar_aluno(id, nome, cpf, email, senha, tel, datacad, datanascimento, sexo, rg, profissao, bairro, cep, rua, num)
                    else:
                        st.error("Preencha todos os campos obrigatórios.")

