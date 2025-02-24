package user.src.template;

import user.src.view.*;
import user.src.model.*;
import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;
import java.util.List;

public class indexUI{
    private static int aluno_id = 0;
    private static String aluno_nome = "";

    public static int menu_visitante(){
        Scanner scanner = new Scanner(System.in);
        int op = 0;
        boolean validInput = false;

        while (!validInput) {
            try {
                System.out.println("\n+------------------------------+");
                System.out.println("|         MENU VISITANTE       |");
                System.out.println("+------------------------------+");
                System.out.println("| 1 - Entrar no sistema        |");
                System.out.println("| 9 - Fim                      |");
                System.out.println("+------------------------------+");

                System.out.print("Informe uma opção: ");
                op = scanner.nextInt();

                if (op == 1 || op == 9) {
                    validInput = true;
                } else {
                    System.out.println("Opção inválida. Por favor, escolha 1 ou 9.");
                }
            } catch (Exception e) {
                System.out.println("Entrada inválida. Por favor, insira um número inteiro.");
                scanner.next(); 
            }
        }

        if (op == 1) {
            indexUI.login();
        }

        return op;
    }

    public static void login(){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Informe o cpf: ");
        String cpf = scanner.nextLine();

        System.out.print("Informe a senha: ");
        String senha = scanner.nextLine();

        Map<String, Object> obj = ViewCliente.login(cpf, senha);

        if (obj == null || obj.isEmpty()){
            System.out.println("E-mail ou senha inválidos");
        } else {
            aluno_id = (int) obj.get("id");
            aluno_nome = (String) obj.get("nome");
        }
    }

    public static int menu_aluno (){
        Scanner scanner = new Scanner(System.in);
        Aluno aluno = ViewCliente.buscarAluno(aluno_id);
        Endereco endereco = ViewCliente.buscarEndereco(aluno_id);

        System.out.println("\n+-----------------------------------------+");
        System.out.println("|           INFORMAÇÕES DO CLIENTE        |");
        System.out.println("+-----------------------------------------+");
        System.out.printf("| %-20s: %-17s |\n", "Nome", aluno.getNome());
        System.out.printf("| %-20s: %-17s |\n", "Email", aluno.getEmail());
        System.out.printf("| %-20s: %-17s |\n", "Telefone", aluno.getTel());
        System.out.printf("| %-20s: %-17s |\n", "CPF", aluno.getCpf());
        System.out.printf("| %-20s: %-17s |\n", "RG", aluno.getRg());
        System.out.printf("| %-20s: %-17s |\n", "Data de Nascimento", aluno.getNascimento());
        System.out.printf("| %-20s: %-17s |\n", "Sexo", aluno.getSexo());
        System.out.printf("| %-20s: %-17s |\n", "Profissão", aluno.getProfissao());
        System.out.printf("| %-20s: %-17s |\n", "Data de Cadastro", aluno.getData_cadastro());
        System.out.printf("| %-20s: %-17s |\n", "Status", ViewCliente.resgatarStatus(aluno_id));
        System.out.println("+-----------------------------------------+");
        System.out.println("|           ENDEREÇO DO CLIENTE           |");
        System.out.println("+-----------------------------------------+");
        System.out.printf("| %-20s: %-17s |\n", "Rua", endereco.getRua());
        System.out.printf("| %-20s: %-17s |\n", "Número", endereco.getNumero());
        System.out.printf("| %-20s: %-17s |\n", "Bairro", endereco.getBairro());
        System.out.printf("| %-20s: %-17s |\n", "CEP", endereco.getCep());
        System.out.println("+-----------------------------------------+");

        System.out.println("\n+----------------------------------------+");
        System.out.println("|              MENU DE OPÇÕES            |");
        System.out.println("+----------------------------------------+");
        System.out.println("| 1 - Atualizar informações              |");
        System.out.println("| 2 - Ver suas medições                  |");
        System.out.println("| 3 - Ver seus treinos                   |");
        System.out.println("| 4 - Ver sua matrícula                  |");
        System.out.println("| 0 - Sair do Sistema                    |");
        System.out.println("| 9 - Encerrar programa                  |");
        System.out.println("+----------------------------------------+");

        System.out.print("Informe uma opção: ");
        int op = scanner.nextInt();

        if (op == 0) {
            indexUI.logout();
        } else if (op == 1) {
            aluno_nome = atualizarUI.main(aluno_id, aluno_nome);
        } else if (op == 2) {
            op = medicoesUI.main(aluno_id);
        } else if (op == 3) {
            op = treinoAlunoUI.main(aluno_id);
        } else if (op == 4) {
            op = matriculaUI.main(aluno_id);
        }
        return op;
    }

    public static void logout(){
        aluno_id = 0;
        aluno_nome = "";
    }

    public static void main(String[] args){
        int op = 0;
        while (op != 9){
            if (aluno_id == 0){
                op = indexUI.menu_visitante();
            } else {
                String nomeFormatado = aluno_nome.length() > 20 ? aluno_nome.substring(0, 17) + "..." : aluno_nome;

                System.out.println("\n+----------------------------------------+");
                System.out.printf("|  Bem-vindo(a) %-23s  |\n", nomeFormatado);
                System.out.println("+----------------------------------------+");
                op = indexUI.menu_aluno();
            }
        }
    }
}