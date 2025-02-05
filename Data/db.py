import sqlite3

# Conecta ao banco de dados (ou cria se não existir)
connection = sqlite3.connect("Data/academia.db")
cursor = connection.cursor()

# Criação das tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT,
    tel TEXT,
    data_cadastro TEXT NOT NULL,
    nascimento TEXT,
    sexo TEXT,
    cpf TEXT,
    rg TEXT,
    profissao TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS enderecos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    bairro TEXT,
    cep TEXT,
    rua TEXT,
    numero TEXT,
    FOREIGN KEY (id_cliente) REFERENCES alunos (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS planos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    valor REAL,
    tempo TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS matriculas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    plano INTEGER NOT NULL,
    data TEXT NOT NULL,
    validade TEXT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES alunos (id),
    FOREIGN KEY (plano) REFERENCES planos (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS pagamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_matricula INTEGER NOT NULL,
    id_cliente INTEGER NOT NULL,
    emissao TEXT NOT NULL,
    vencimento TEXT NOT NULL,
    data_pagamento TEXT,
    valor REAL NOT NULL,
    pago BOOLEAN NOT NULL,
    FOREIGN KEY (id_matricula) REFERENCES matriculas (id),
    FOREIGN KEY (id_cliente) REFERENCES alunos (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS medicoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    data TEXT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES alunos (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS medidas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_medicoes INTEGER NOT NULL,
    id_partcorpo INTEGER NOT NULL,
    valor REAL NOT NULL,
    FOREIGN KEY (id_medicoes) REFERENCES medicoes (id),
    FOREIGN KEY (id_partcorpo) REFERENCES partcorpos (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS partcorpos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    unidade TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS treinosalunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_aluno INTEGER NOT NULL,
    data TEXT NOT NULL,
    data_final TEXT,
    FOREIGN KEY (id_aluno) REFERENCES alunos (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS treinos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_musculo INTEGER NOT NULL,
    id_treino INTEGER,
    descricao TEXT,
    FOREIGN KEY (id_musculo) REFERENCES musculos (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS musculos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
''')

# Commit para salvar as alterações
connection.commit()

# Fechar a conexão com o banco de dados
cursor.close()
connection.close()

print("Tabelas criadas com sucesso!")