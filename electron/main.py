from flask import Flask, jsonify, request
import models
import re
from datetime import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

# Função para inserir aluno
@app.route('/api/aluno', methods=['POST'])
def inserir_aluno():
    data = request.get_json()  # Recebe os dados como JSON
    nome = data['nome']
    email = data['email']
    tel = data['tel']
    data_cadastro = data['data_cadastro']
    nascimento = data['nascimento']
    sexo = data['sexo']
    cpf = data['cpf']
    rg = data['rg']
    profissao = data['profissao']
    bairro = data['bairro']
    cep = data['cep']
    rua = data['rua']
    numero = data['numero']
    
    aluno = models.Aluno(0, nome, email, tel, data_cadastro, nascimento, sexo, cpf, rg, profissao)
    l = models.Alunos.listar()
    
    # Remover caracteres não numéricos do CPF
    cpf = re.sub(r'\D', '', cpf)
    
    liberado = True
    for alu in l:
        if False:
            liberado = False
            break

    if liberado:
        models.Alunos.inserir(aluno)
        la = models.Alunos.listar()

        for alu in la:
            if alu.cpf == cpf:
                endereco = models.Endereco(0, alu.id, bairro, cep, rua, numero)
                models.Enderecos.inserir(endereco)
                return jsonify({"message": "Aluno e endereço inseridos com sucesso!"}), 201
        return jsonify({"message": "Aluno inserido, mas o endereço não foi adicionado."}), 400
    else:
        return jsonify({"message": "CPF já cadastrado!"}), 400

# Função para listar alunos
@app.route('/api/alunos', methods=['GET'])
def listar_alunos():
    alunos = models.Alunos.listar()
    alunos_list = [aluno.to_dict() for aluno in alunos]  # Supondo que você tenha um método to_dict no seu modelo
    return jsonify(alunos_list), 200

# Função para listar endereços
@app.route('/api/enderecos', methods=['GET'])
def listar_enderecos():
    enderecos = models.Enderecos.listar()
    enderecos_list = [endereco.to_dict() for endereco in enderecos]  # Supondo que você tenha um método to_dict no seu modelo
    return jsonify(enderecos_list), 200

# Função para inserir matrícula
@app.route('/api/matricula', methods=['POST'])
def inserir_matricula():
    data = request.get_json()  # Recebe os dados como JSON
    id_aluno = data['id_aluno']
    id_plano = data['id_plano']
    data_matricula = data['data']
    validade = data['validade']
    
    try:
        # Chama a função de inserção da matrícula
        inserir_matricula(id_aluno, id_plano, data_matricula, validade)
        return jsonify({"message": "Matrícula inserida com sucesso!"}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

# Função para calcular validade
@app.route('/api/calcular_validade', methods=['POST'])
def calcular_validade():
    data = request.get_json()  # Recebe os dados como JSON
    data_inicial = data['data_inicial']
    tempo = data['tempo']
    
    validade = calcular_validade(data_inicial, tempo)
    return jsonify({"validade": validade}), 200

if __name__ == '__main__':
    app.run(debug=True)
