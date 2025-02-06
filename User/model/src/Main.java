import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class Main {
    public static void main(String[] args) {
        int id = 1;
        String name = "John Doe";
        String email = "r1GfB@example.com";
        String tel = "(12) 3456-7890";

        LocalDate dataCadastro = LocalDate.now();
        LocalDate nascimento = LocalDate.of(1990, 1, 1);

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        String dataCadastroStr = dataCadastro.format(formatter);
        String nascimentoStr = nascimento.format(formatter);

        String sexo = "M";
        String cpf = "713.280.564-90";
        String rg = "123456789";
        String profissao = "Programador";

        Aluno aluno = new Aluno(id, name, email, tel, dataCadastroStr, nascimentoStr, sexo, cpf, rg, profissao);
        aluno.setId(50);

        // System.out.println(aluno);

        // Alunos alunos = new Alunos();
        // alunos.inserir(aluno);

        id = 1;
        int id_cliente = 1;
        String bairro = "Centro";
        String cep = "12345678";
        String rua = "Rua Principal";
        String numero = "123";

        Endereco endereco = new Endereco(id, id_cliente, bairro, cep, rua, numero);
        endereco.setId(50);

        // System.out.println(endereco);

        // Enderecos enderecos = new Enderecos();
        // enderecos.inserir(endereco);

        id = 1;
        id_cliente = 1;
        String plano = "semestral";
        String data = "01/01/2025";
        String validade = "isso funciona?";

        Matricula matricula = new Matricula(id, id_cliente, plano, data, validade);
        matricula.setId(50);

        // System.out.println(matricula);

        // Matriculas matriculas = new Matriculas();
        // matriculas.inserir(matricula);

        id = 1;
        id_cliente = 1;
        data = "01/01/2025";

        Medicao medicao = new Medicao(id, id_cliente, data);
        medicao.setId(50);

        // System.out.println(medicao);

        // Medicoes medicoes = new Medicoes();
        // medicoes.inserir(medicao);

        id = 1;
        int id_medicoes = 1;
        int id_partcorpo = 1;
        double valor = 10.0;

        Medida medida = new Medida(id, id_medicoes, id_partcorpo, valor);
        medida.setId(50);

        // System.out.println(medida);

        // Medidas medidas = new Medidas();
        // medidas.inserir(medida);

        id = 1;
        String nome = "Peito";
        String unidade = "cm";

        ParteCorpo parteCorpo = new ParteCorpo(id, nome, unidade);
        parteCorpo.setId(50);

        // System.out.println(parteCorpo);

        // PartesCorpo partescorpo = new PartesCorpo();
        // partescorpo.inserir(parteCorpo);

        id = 1;
        int id_matricula = 1;
        id_cliente = 1;
        String emissao = "01/01/2025";
        String vencimento = "01/01/2025";
        String data_pagamento = "01/01/2025";
        valor = 10.0;
        boolean pago = true;

        Pagamento pagamento = new Pagamento(id, id_matricula, id_cliente, emissao, vencimento, data_pagamento, valor, pago);
        pagamento.setId(50);

        // System.out.println(pagamento);

        // Pagamentos pagamentos = new Pagamentos();
        // pagamentos.inserir(pagamento);

        id = 1;
        nome = "Semestral";
        valor = 10.0;
        String tempo = "ano";

        Plano planow = new Plano(id, nome, valor, tempo);
        planow.setId(50);

        // System.out.println(planow);

        // Planos planos = new Planos();
        // planos.inserir(planow);

        id = 1;
        int id_aluno = 1;
        data = "01/01/2025";
        String data_final = "01/01/2025";

        TreinoAluno treinoAluno = new TreinoAluno(id, id_aluno, data, data_final);
        treinoAluno.setId(50);

        // System.out.println(treinoAluno);

        // TreinosAlunos treinoalunos = new TreinosAlunos();
        // treinoalunos.inserir(treinoAluno);

        id = 1;
        int id_musculo = 1;
        int id_treino = 1;
        String descricao = "DESEJO DE MATAR";

        Treino treino = new Treino(id, id_musculo, id_treino, descricao);
        treino.setId(50);

        System.out.println(treino);

        Treinos treinos = new Treinos();
        treinos.inserir(treino);

        id = 1;
        nome = "Quadriceps";

        Musculo musculo = new Musculo(id, nome);
        musculo.setId(50);

        // System.out.println(musculo);

        // Musculos musculos = new Musculos();
        // musculos.inserir(musculo)
    }
}
