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
        
        System.out.println("Informe uma opção: ");
        int op = scanner.nextInt();
        if (op == 1) {
            indexUI.visitante_entrar_no_sistema();
        }
        return op;
    }

    public static void visitante_entrar_no_sistema(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Informe o cpf: ");
        String cpf = scanner.nextLine();

        System.out.println("Informe a senha: ");
        String senha = scanner.nextLine();

        Map<String, Object> obj = ViewCliente.login(cpf, senha);

        if (obj == null || obj.isEmpty()){
            System.out.println("E-mail ou senha inválidos");
        } else {
            aluno_id = (int) obj.get("id");
            aluno_nome = (String) obj.get("nome");
        }
    }

    public static int menu_cliente (){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Informações do cliente....");
        System.out.println("1 - Atualizar, 2 - Ver suas medidas, 3 - Ver seus treinos, 4 - Ver sua matricula");
        System.out.println("0 - Sair, 99 - Fim");

        System.out.println("\nInforme uma opção: ");
        int op = scanner.nextInt();

        if (op == 0){
            indexUI.sair_do_sistema();
        }
        return op;
    }

    public static void sair_do_sistema(){
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
                op = indexUI.menu_cliente();
            }
        }
    }
}