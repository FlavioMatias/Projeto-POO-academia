package user.src.model;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // int id = 1;
        // String name = "Bostinha";
        // String email = "r1GfB@example.com";
        // String tel = "84996581121";
        // String dataCadastro = "12/02/2025";
        // String nascimento = "12/02/2025";
        // String sexo = "M";
        // String cpf = "713.280.564-90";
        // String rg = "123456789";
        // String profissao = "Programador";
        // String senha = "12345678";

        // Aluno aluno = new Aluno(id, name, senha, email, tel, dataCadastro, nascimento, sexo, cpf, rg, profissao);
        // System.out.println(aluno);




        // int id = 1;
        // String nome = "Semestral";
        // double valor = 50;
        // String tempo = "6 meses";

        // Plano plano = new Plano(id, nome, valor, tempo);
        // System.out.println(plano);

        // Planos planos = new Planos();
        // planos.inserir(plano);

        // System.out.println(planos.listar());




        // int id = 1;
        // int id_cliente = 1;
        // int id_plano = 1;
        // String data = "19/02/2025";
        // String validade = "31/08/2025";
        // boolean ativo = true;

        // Matricula matricula = new Matricula(id, id_cliente, id_plano, data, validade, ativo);
        // System.out.println(matricula);

        // Matriculas matriculas = new Matriculas();
        // matriculas.inserir(matricula);

        // System.out.println(matriculas.listar());





        // int id = 1;
        // String nome = "Braco";
        // String unidade = "cm";

        // ParteCorpo partecorpo1 = new ParteCorpo(id, nome, unidade);

        // id = 2;
        // nome = "Perna";
        // unidade = "cm";

        // ParteCorpo partecorpo2 = new ParteCorpo(id, nome, unidade);

        // id = 3;
        // nome = "Quadril";
        // unidade = "cm";

        // ParteCorpo partecorpo3 = new ParteCorpo(id, nome, unidade);


        // PartesCorpo partescorpo = new PartesCorpo();
        // partescorpo.inserir(partecorpo1);
        // partescorpo.inserir(partecorpo2);
        // partescorpo.inserir(partecorpo3);

        // System.out.println(partescorpo.listar());




        // int id = 1;
        // int id_aluno = 1;
        // String data = "19/02/2025";
        // boolean ativa = true;

        // Medicao medicao1 = new Medicao(id, id_aluno, data, ativa);

        
        // id = 2;
        // id_aluno = 1;
        // data = "19/01/2025";
        // ativa = true;

        // Medicao medicao2 = new Medicao(id, id_aluno, data, ativa);

        // id = 3;
        // id_aluno = 1;
        // data = "19/12/2024";
        // ativa = true;

        // Medicao medicao3 = new Medicao(id, id_aluno, data, ativa);

        // Medicoes medicoes = new Medicoes();
        // medicoes.inserir(medicao1);
        // medicoes.inserir(medicao2);
        // medicoes.inserir(medicao3);

        // System.out.println(medicoes.listar());




        // int id = 1;
        // int id_medicao = 3;
        // int id_partcorpo = 1;
        // double valor = 37;

        // Medida medida1 = new Medida(id, id_medicao, id_partcorpo, valor);
        
        // id = 2;
        // id_medicao = 3;
        // id_partcorpo = 2;
        // valor = 50;

        // Medida medida2 = new Medida(id, id_medicao, id_partcorpo, valor);

        // id = 3;
        // id_medicao = 3;
        // id_partcorpo = 3;
        // valor = 100;

        // Medida medida3 = new Medida(id, id_medicao, id_partcorpo, valor);

        // Medidas medidas = new Medidas();

        // medidas.inserir(medida1);
        // medidas.inserir(medida2);
        // medidas.inserir(medida3);

        // System.out.println(medidas.listar());




        int id = 1;
        int id_matricula = 1;
        int id_cliente = 1;
        String emissao = "18/02/2025";
        String vencimento = "18/03/2025";
        String data_pagamento = "19/02/2025";
        double valor = 50;
        boolean pago = true;

        Pagamento pagamento1 = new Pagamento(id, id_matricula, id_cliente, emissao, vencimento, data_pagamento, valor, pago);

        id = 2;
        id_matricula = 1;
        id_cliente = 1;
        emissao = "18/01/2025";
        vencimento = "18/02/2025";
        data_pagamento = "";
        valor = 50;
        pago = false;

        Pagamento pagamento2 = new Pagamento(id, id_matricula, id_cliente, emissao, vencimento, data_pagamento, valor, pago);

        id = 3;
        id_matricula = 1;
        id_cliente = 1;
        emissao = "18/02/2025";
        vencimento = "18/04/2025";
        data_pagamento = "";
        valor = 50;
        pago = false;

        Pagamento pagamento3 = new Pagamento(id, id_matricula, id_cliente, emissao, vencimento, data_pagamento, valor, pago);

        Pagamentos pagamentos = new Pagamentos();

        pagamentos.inserir(pagamento1);
        pagamentos.inserir(pagamento2);
        pagamentos.inserir(pagamento3);

        System.out.println(pagamentos.listar());
    }
}
