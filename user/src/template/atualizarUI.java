package user.src.template;

import user.src.view.*;
import java.util.Scanner;

public class atualizarUI {
    public static String main(int aluno_id) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Atualizar dados do perfil:");

        System.out.print("Informe o novo nome: ");
        String nome = scanner.nextLine();

        System.out.print("Informe o novo email: ");
        String email = scanner.nextLine();

        System.out.print("Informe a nova senha: ");
        String senha = scanner.nextLine();

        System.out.print("Informe o novo telefone: ");
        String tel = scanner.nextLine();

        System.out.print("Informe a nova data de cadastro: ");
        String data_cadastro = scanner.nextLine();

        System.out.print("Informe a nova data de nascimento: ");
        String nascimento = scanner.nextLine();

        System.out.print("Informe o novo sexo: ");
        String sexo = scanner.nextLine();

        System.out.print("Informe o novo cpf: ");
        String cpf = scanner.nextLine();

        System.out.print("Informe o novo rg: ");
        String rg = scanner.nextLine();

        System.out.print("Informe a nova profissao: ");
        String profissao = scanner.nextLine();

        try {
            ViewCliente.atualizarAluno(aluno_id, nome, email, senha, tel, data_cadastro, nascimento, sexo, cpf, rg, profissao);
            System.out.println("Aluno atualizado com sucesso!");
        } catch (Exception e) {
            System.err.println("Erro ao atualizar o aluno: " + e.getMessage());
            e.printStackTrace();
        } finally {
            return nome;
        }
    }
}