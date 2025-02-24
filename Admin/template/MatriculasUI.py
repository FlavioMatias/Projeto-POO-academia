from Admin.view import *
import streamlit as st


class MatriculasUI:
    __page = 'matriculas'
    __last_matricula = None

    @classmethod
    def main(cls):
        if cls.__page == 'matriculas':
            src = st.text_input('buscar matricula', placeholder="digite o id da matricula")
        if cls.__page == 'matriculas':
            with st.container(border=True):
                cls.matricular_aluno()
            if not src:
                for matricula in MatriculaView.listar_matriculas():
                    aluno = AlunosView.buscar_aluno(matricula.id_aluno)
                    plano = PlanosView.buscar(matricula.plano)
                    with st.container(border=True):
                        dados, detalhe = st.columns((6,1))
                        with dados:
                            st.write('ID da matricula:', matricula.id)
                            st.write(f'Aluno: {aluno.id} - {aluno.nome}')
                            st.write(f'Plano: {plano.id} - {plano.nome}')
                            st.write('Data da matricula:', matricula.data)
                            st.write('Valida ate:', matricula.validade)

                        with detalhe:
                            if st.button('datalhes', key=f'detalhe{matricula.id}'):
                                cls.__page = 'detalhes'
                                cls.__last_matricula = matricula
                                st.rerun()
                            if st.button('Cancelar', key=f'cancelar{matricula.id}'):
                                MatriculaView.atualizar_matricula(matricula.id, matricula.id_aluno, matricula.plano, matricula.data, matricula.validade, False)
                                st.rerun()

            else:
                for matricula in MatriculaView.buscar_matricula(int(src)):
                    aluno = AlunosView.buscar_aluno(matricula.id_aluno)
                    plano = PlanosView.buscar(matricula.plano)
                    with st.container(border=True):
                        dados, detalhe = st.columns((6,1))
                        with dados:
                            st.write('ID da matricula:', matricula.id)
                            st.write(f'Aluno: {aluno.id} - {aluno.nome}')
                            st.write(f'Plano: {plano.id} - {plano.nome}')
                            st.write('Data da matricula:', matricula.data)
                            st.write('Valida ate:', matricula.validade)

                        with detalhe:
                            if st.button('datalhes', key=f'detalhe{matricula.id}'):
                                cls.__page = 'detalhes'
                                cls.__last_matricula = matricula
                                st.rerun()
                            if st.button('Cancelar', key=f'cancelar{matricula.id}'):
                                MatriculaView.atualizar_matricula(matricula.id, matricula.id_aluno, matricula.plano, matricula.data, matricula.validade, False)
                                st.rerun()


        if cls.__page == 'detalhes':
            cls.detalhes_matricula(cls.__last_matricula)
    
            if st.button('voltar'):
                cls.__page = 'matriculas'
                cls.__last_matricula = None
                st.rerun()

    @classmethod
    def detalhes_matricula(cls, matricula):
        aluno = AlunosView.buscar_aluno(matricula.id_aluno)
        plano = PlanosView.buscar(matricula.plano)
        endereço_aluno = AlunosView.buscar_endereco_aluno(aluno.id) 
        with st.container(border=True):
            st.subheader("Detalhes da Matrícula")
            st.write(f"**ID da Matrícula:** {matricula.id}")
            st.write(f"**ID do Aluno:** {matricula.id_aluno}")
            st.write(f"**Data de Início:** {matricula.data}")
            st.write(f"**Validade até:** {matricula.validade}")
            st.write(f"**Status da Matrícula:** {'Ativa' if matricula.ativa else 'Inativa'}")

        with st.container(border=True):
            st.subheader("Detalhes do Aluno")
            st.write(f"**ID do Aluno:** {aluno.id}")
            st.write(f"**Nome:** {aluno.nome}")
            st.write(f"**Email:** {aluno.email}")
            st.write(f"**Telefone:** {aluno.tel}")
            st.write(f"**Data de Cadastro:** {aluno.data_cadastro}")
            st.write(f"**Data de Nascimento:** {aluno.nascimento}")
            st.write(f"**Sexo:** {aluno.sexo}")
            st.write(f"**CPF:** {aluno.cpf}")
            st.write(f"**RG:** {aluno.rg}")
            st.write(f"**Profissão:** {aluno.profissao}")
            if endereço_aluno:
                st.subheader('Endereço:')
                st.write(f"**ID do Endereço:** {endereço_aluno.id}")
                st.write(f"**Bairro:** {endereço_aluno.bairro}")
                st.write(f"**CEP:** {endereço_aluno.cep}")
                st.write(f"**Rua:** {endereço_aluno.rua}")
                st.write(f"**Número:** {endereço_aluno.numero}")
            else:
                st.write("***Endereço Não Registrado***")
        with st.container(border=True):
                st.subheader("Detalhes do Plano")
                st.write(f"**ID do Plano:** {plano.id}")
                st.write(f"**Nome do Plano:** {plano.nome}")
                st.write(f"**Valor do Plano:** R$ {plano.valor:.2f}")
                st.write(f"**Duração do Plano:** {plano.tempo}")

    @classmethod
    def matricular_aluno(cls):
        id_aluno_matriculados = [matricula.id_aluno for matricula in MatriculaView.listar_matriculas() if matricula.ativa]
        aluno_opcoes = [f"{aluno.id} | {aluno.nome}" for aluno in AlunosView.listar_alunos() if aluno.id not in id_aluno_matriculados]
        planos = [f'{plano.id} | {plano.nome} - R${plano.valor:.2f} | {plano.tempo}' for plano in PlanosView.listar_planos()]
        id_plano_selecionado = None
        id_aluno_selecionado = None
        with st.expander("matricular aluno", expanded=False):
            aluno_selecionado = st.selectbox('Escolha o aluno', aluno_opcoes)
            
            if aluno_selecionado:
                id_aluno_selecionado = int(aluno_selecionado.split(" | ")[0])
            else:
                st.info('Nenhum aluno para matricular')
                
            plano_selecionado = st.selectbox('Escolha o plano', planos)

            if plano_selecionado:
                id_plano_selecionado = int(plano_selecionado.split(" | ")[0])
            else:
                st.info('Nenhum plano para registrado')
                
            if st.button("matricular"):
                if not id_aluno_selecionado and id_plano_selecionado:
                    st.error('Selecione um aluno e um plano')
                else:
                    View.matricular_aluno(id_aluno_selecionado, id_plano_selecionado)
                    st.success('matricula realizada')



