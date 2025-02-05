from .. import models

aluno_exemplo = models.Aluno(
    id=1,
    nome="João Da Silva",
    email="joao.silva@example.com",
    tel="(11) 98765-4321",
    data_cadastro="05/02/2025",
    nascimento="25/12/2004",
    sexo="M",
    cpf="707.534.174.05",
    rg="12.345.678-9",
    profissao="Engenheiro de Software"
)


#models.Alunos.inserir(aluno_exemplo)

alunos = models.Alunos.listar()

for aluno in alunos:
    print(aluno)