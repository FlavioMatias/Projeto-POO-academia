from Admin.view.adm_view import View 
import streamlit as st
from datetime import datetime
class UI:
    @staticmethod
    def main():
        st.title("Gestão de Alunos")

        if "pagina" not in st.session_state:
            st.session_state.pagina = "home"
        if "aluno_selecionado" not in st.session_state:
            st.session_state.aluno_selecionado = None

        if st.session_state.pagina == "home":
            UI.home()
        elif st.session_state.pagina == "matricula":
            UI.matricular()

    @staticmethod
    def home():
        menu = st.sidebar.selectbox("Menu", ["Inserir Aluno", "Listar Alunos", "Alunos Matriculados"])

        if menu == "Inserir Aluno":
            UI.inserir_aluno()
        elif menu == "Listar Alunos":
            UI.listar_alunos()
        elif menu == "Alunos Matriculados":
            UI.listar_matriculados()

    @staticmethod
    def listar_matriculados():
        alunos = View.listar_alunos()
        matriculas = View.listar_matriculas()

        # Criando um conjunto de IDs dos alunos matriculados (usando set para busca eficiente)
        alunos_matriculados = {matricula.id_cliente for matricula in matriculas}

        # Iterando apenas sobre os alunos e verificando se o aluno está matriculado
        for aluno in alunos:
            if aluno.id in alunos_matriculados:
                # Encontrar todas as matrículas do aluno
                matriculas_aluno = [matricula for matricula in matriculas if matricula.id_cliente == aluno.id]

                with st.container(border=True):
                    st.write(aluno.to_dict())  # Exibindo os dados do aluno
                    st.subheader("Matrículas")  # Título para a seção de matrículas

                    # Exibe todas as matrículas do aluno
                    if matriculas_aluno:
                        for matricula in matriculas_aluno:
                            st.write(matricula.to_dict())  # Exibindo os dados de cada matrícula
                    else:
                        st.write("Este aluno não possui matrícula.")


    @staticmethod
    def inserir_aluno():
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
        bairro = st.text_input("Bairro")
        cep = st.text_input("CEP")
        rua = st.text_input("Rua")
        numero = st.text_input("Número da Casa")

        if st.button("Inserir Aluno"):
            try:
                View.inserir_aluno(nome, email, tel, data_cadastro, nascimento, sexo, cpf, rg, profissao, bairro, cep, rua, numero)
                st.success("Aluno inserido com sucesso!")
            except Exception as e:
                st.error(f"Ocorreu um erro: {e}")

    @staticmethod
    def listar_alunos():
        st.header("Lista de Alunos")
        alunos = View.listar_alunos()
        enderecos = View.listar_endereços()

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

                    enderecos_aluno = [endereco for endereco in enderecos if endereco.id_cliente == aluno.id]

                    if enderecos_aluno:
                        for endereco in enderecos_aluno:
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

                    if st.button(f"Matricular {aluno.nome}", key=f"matricular_{aluno.id}"):
                        st.session_state.pagina = "matricula"
                        st.session_state.aluno_selecionado = aluno
                        st.rerun()
        else:
            st.write("Nenhum aluno cadastrado.")

    @staticmethod
    def matricular():
        aluno = st.session_state.aluno_selecionado
        print(aluno)
        planos = View.listar_planos()
        if aluno:
            st.header(f"Matricular Aluno: {aluno.nome}")

            plano_escolhido = st.selectbox("Selecione o Curso", [plano.nome for plano in planos])
            plano = next((p for p in planos if p.nome == plano_escolhido), None)
            data_matricula = st.text_input("Data de Matrícula", value=datetime.today().strftime('%d/%m/%Y'))

            if st.button("Confirmar Matrícula"):
                View.inserir_matricula(aluno.id, plano.id, data_matricula, plano.tempo)
                st.success(f"Aluno {aluno.nome, aluno.id} matriculado com sucesso!")

            if st.button("Voltar"):
                UI.voltar()

    @staticmethod
    def voltar():
        """Função para voltar à tela inicial"""
        st.session_state.pagina = "home"
        st.session_state.aluno_selecionado = None
        st.rerun()
