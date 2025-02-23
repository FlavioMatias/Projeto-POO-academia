package user.src.template;

import user.src.view.*;
import java.util.Scanner;

public class atualizarUI {
    public static String main(int aluno_id, String aluno_nome) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("\n+----------------------------------------+");
        System.out.println("|       ATUALIZAR DADOS DO PERFIL        |");
        System.out.println("+----------------------------------------+");

        String nome = solicitarEntrada(scanner, "Informe o novo nome: ");
        String email = solicitarEntrada(scanner, "Informe o novo email: ");
        String senha = solicitarEntrada(scanner, "Informe a nova senha: ");
        String tel = solicitarEntrada(scanner, "Informe o novo telefone: ");
        String data_cadastro = solicitarEntrada(scanner, "Informe a nova data de cadastro: ");
        String nascimento = solicitarEntrada(scanner, "Informe a nova data de nascimento: ");
        String sexo = solicitarEntrada(scanner, "Informe o novo sexo: ");
        String cpf = solicitarEntrada(scanner, "Informe o novo CPF: ");
        String rg = solicitarEntrada(scanner, "Informe o novo RG: ");
        String profissao = solicitarEntrada(scanner, "Informe a nova profissão: ");
        String bairro = solicitarEntrada(scanner, "Informe o novo bairro: ");
        String cep = solicitarEntrada(scanner, "Informe o novo cep: ");
        String rua = solicitarEntrada(scanner, "Informe a nova rua: ");
        String numero = solicitarEntrada(scanner, "Informe o novo numero: ");

        try {
            ViewCliente.atualizarAluno(aluno_id, nome, email, senha, tel, data_cadastro, nascimento, sexo, cpf, rg, profissao, bairro, cep, rua, numero);
            System.out.println("\n+----------------------------------------+");
            System.out.println("|  Aluno atualizado com sucesso!         |");
            System.out.println("+----------------------------------------+");
            aluno_nome = nome;
        } catch (Exception e) {
            System.err.println("\n+----------------------------------------+");
            System.err.println("|  Erro ao atualizar o aluno:             |");
            System.err.println("+----------------------------------------+");
            System.err.println("Mensagem de erro: " + e.getMessage());
        }

        return aluno_nome;
    }

    private static String solicitarEntrada(Scanner scanner, String mensagem) {
        System.out.print("| " + mensagem);
        return scanner.nextLine();
    }
}