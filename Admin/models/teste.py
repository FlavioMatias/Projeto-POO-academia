from alunos import Aluno
from CRUD import Alunos

id = 666
nome = "Icaro"
email = "icaro@email.com"
tel = "(99) 9999-9999"
data_cadastro = "05/02/2025"
nascimento = "15/02/2005"
sexo = "M"
cpf = "713.280.564-90"
rd = "123456789"
profissao = "nada"

# aluno1 = Aluno(id, nome, email, tel, data_cadastro, nascimento, sexo, cpf, rd, profissao)
# print(aluno1)
# Alunos.inserir(aluno1)

for x in Alunos.listar():
    print(x)