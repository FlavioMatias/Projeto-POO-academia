package user.src.template;

import user.src.view.*;
import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;
import java.util.List;

public class indexUI{
    private static int aluno_id = 0;
    private static String aluno_nome = "";

    public static int menu_visitante(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("1 - Entrar no sistema, 9 - Fim");
        
        System.out.print("Informe uma opção: ");
        int op = scanner.nextInt();
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
        System.out.println("Informações do cliente....");
        System.out.println("1 - Atualizar, 2 - Ver suas medidas, 3 - Ver seus treinos, 4 - Ver sua matricula");
        System.out.println("0 - Sair, 9 - Fim");

        System.out.print("Informe uma opção: ");
        int op = scanner.nextInt();

        if (op == 0) {
            indexUI.logout();
        } else if (op == 1) {
            aluno_nome = atualizarUI.main(aluno_id);
        } else if (op == 2) {
            op = medicoesUI.main(aluno_id);
        } else if (op == 3) {
            // ver seus treinos
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
                System.out.println("\nBem-vindo(a) " + aluno_nome);
                op = indexUI.menu_aluno();
            }
        }
    }
}