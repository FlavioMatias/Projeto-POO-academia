
document.getElementById('formAluno').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const alunoData = {
        nome: document.getElementById('nome').value,
        email: document.getElementById('email').value,
        tel: document.getElementById('tel').value,
        data_cadastro: document.getElementById('data_cadastro').value,
        nascimento: document.getElementById('nascimento').value,
        sexo: document.getElementById('sexo').value,
        cpf: document.getElementById('cpf').value,
        rg: document.getElementById('rg').value,
        profissao: document.getElementById('profissao').value,
        bairro: document.getElementById('bairro').value,
        cep: document.getElementById('cep').value,
        rua: document.getElementById('rua').value,
        numero: document.getElementById('numero').value
    };

    fetch('http://127.0.0.1:5000/api/aluno', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(alunoData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerHTML = `<strong>${data.message}</strong>`;
    })
    .catch(error => {
        document.getElementById('response').innerHTML = `<strong>Erro: ${error.message}</strong>`;
    });
});

document.getElementById('listarAlunos').addEventListener('click', function() {
    fetch('http://127.0.0.1:5000/api/alunos')
    .then(response => response.json())
    .then(alunos => {
        let alunoList = '<ul>';
        alunos.forEach(aluno => {
            alunoList += `<li class = "user" >
                            <div class="aluno_container">
                                <h3>${aluno.nome}</h3>
                                <ul>
                                    <li>email: ${aluno.nome}</li>
                                    <li>telefone: ${aluno.tel}</li>
                                    <li>data de cadastro: ${aluno.data_cadastro}</li>
                                <ul>
                                <button onclick="#">Detalhes</button>
                            </div>
             
                        </li>`;
        });
        alunoList += '</ul>';
        document.getElementById('response').innerHTML = alunoList;
    })
    .catch(error => {
        document.getElementById('response').innerHTML = `<strong>Erro: ${error.message}</strong>`;
    });
});