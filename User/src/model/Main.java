import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // System.out.print("Digite o ID: ");
        // int id = scanner.nextInt();
        // scanner.nextLine();

        // System.out.print("Digite o nome: ");
        // String name = scanner.nextLine();

        // System.out.print("Digite o e-mail: ");
        // String email = scanner.nextLine();

        // System.out.print("Digite o telefone: ");
        // String tel = scanner.nextLine();

        // System.out.print("Digite a data de cadastro (dd/mm/yyyy): ");
        // String dataCadastro = scanner.nextLine();

        // System.out.print("Digite a data de nascimento (dd/mm/yyyy): ");
        // String nascimento = scanner.nextLine();

        // System.out.print("Digite o sexo (M/F): ");
        // String sexo = scanner.nextLine();

        // System.out.print("Digite o CPF: ");
        // String cpf = scanner.nextLine();

        // System.out.print("Digite o RG: ");
        // String rg = scanner.nextLine();

        // System.out.print("Digite a profissão: ");
        // String profissao = scanner.nextLine();

        int id = 1;
        String name = "Bostinha";
        String email = "r1GfB@example.com";
        String tel = "84996581121";
        String dataCadastro = "12/02/2025";
        String nascimento = "12/02/2025";
        String sexo = "M";
        String cpf = "713.280.564-90";
        String rg = "123456789";
        String profissao = "Programador";

        Aluno aluno = new Aluno(id, name, email, tel, dataCadastro, nascimento, sexo, cpf, rg, profissao);
        aluno.setId(50);

        // System.out.println(aluno);

        Alunos alunos = new Alunos();
        // alunos.inserir(aluno);

        System.out.println(alunos.listar());

        // id = aluno.getId();
        // name = "Jorge";
        // email = "jorge@email.com";
        // tel = "(99) 9999-9999";
        // dataCadastro = "11/02/2025";
        // nascimento = "11/02/2025";
        // sexo = "F";
        // cpf = "707.534.174-05";
        // rg = "123456789";
        // profissao = "nao tem";

        // Aluno aluno2 = new Aluno(id, name, email, tel, dataCadastro, nascimento, sexo, cpf, rg, profissao);

        // alunos.atualizar(aluno2);

        // System.out.println(alunos.listar());

        id = 1;
        int id_cliente = 1;
        String bairro = "Centro";
        String cep = "12345-678";
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
        String data = "12/02/2025";
        String validade = "12/02/2025";

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

        // System.out.println(medidas.listar());

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
        String emissao = "11/01/2025";
        String vencimento = "12/01/2025";
        String data_pagamento = "12/01/2025";
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
        String data_final = "13/02/2025";

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

        // System.out.println(treino);

        // Treinos treinos = new Treinos();
        // treinos.inserir(treino);

        id = 1;
        nome = "Quadriceps";

        Musculo musculo = new Musculo(id, nome);
        musculo.setId(50);

        // System.out.println(musculo);

        // Musculos musculos = new Musculos();
        // musculos.inserir(musculo)

        scanner.close();
    }
}
