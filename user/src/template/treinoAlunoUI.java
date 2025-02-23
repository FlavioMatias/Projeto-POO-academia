package user.src.template;

import user.src.view.*;
import user.src.model.*;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class treinoAlunoUI {
    public static int main (int id_aluno) {
        Scanner scanner = new Scanner(System.in);
        List<TreinoAluno> treinoalunos = ViewCliente.listarTreinosAluno(id_aluno);
        int op = 0;
        boolean validInput = false;

        while (!validInput) {
            try {
                System.out.println("\n+----------------------------------------------------------+");
                System.out.println("|                SEUS TREINOS CADASTRADOS                  |");
                System.out.println("+----------------------------------------------------------+");

                if (treinoalunos.isEmpty()) {
                    System.out.println("| Nenhuma medição cadastrada.           |");
                } else {
                    for (TreinoAluno ta : treinoalunos) {
                        System.out.printf("| ID: %-4d | Aluno: %-4d | Data: %-10s | Ativo: %-5s |\n",
                            ta.getId(),
                            ta.getIdAluno(),
                            ta.getData(),
                            ta.getAtiva() ? "Sim" : "Não");
                    }
                }

                System.out.println("+----------------------------------------------------------+");
                System.out.println("| 1 - Detalhar                                             |");
                System.out.println("| 2 - Voltar                                               |");
                System.out.println("| 9 - Fim                                                  |");
                System.out.println("+----------------------------------------------------------+");
                System.out.print("Informe sua opção: ");
                op = scanner.nextInt();

                if (op == 1){
                    boolean entradaValida = false;
                    int id_treinoAluno = 0;

                    System.out.println("\n+----------------------------------------+");
                    System.out.println("|       DETALHAR TREINOS POR ID          |");
                    System.out.println("+----------------------------------------+");

                    while (!entradaValida) {
                        try {
                            System.out.print("| Digite o ID da medição que deseja detalhar: ");
                            id_treinoAluno = scanner.nextInt();
                            entradaValida = true;
                        } catch (Exception e){
                            System.out.println("Entrada inválida. Por favor, insira um número inteiro.");
                            scanner.next();
                        }
                    }

                    TreinoAluno treinoaluno_selecionado = null;
                    for (TreinoAluno ta : treinoalunos) {
                        if (ta.getId() == id_treinoAluno) {
                            treinoaluno_selecionado = ta;
                            break;
                        }
                    }

                    if (treinoaluno_selecionado != null) {
                        treinoAlunoUI.detalharTreinoAluno(treinoaluno_selecionado, id_aluno);

                        boolean sair = false;

                        while (!sair) {
                            System.out.println("+------------------------------------------+");
                            System.out.println("| 1 - Sair                                 |");
                            System.out.println("+------------------------------------------+");

                            try {
                                System.out.print("Informe uma opção: ");
                                op = scanner.nextInt();

                                switch (op) {
                                    case 1:
                                        System.out.println("Saindo do menu de detalhes...");
                                        sair = true;
                                        break;
                                    default:
                                        System.out.println("Opção inválida. Tente novamente.");
                                        break;
                                }
                            } catch (Exception e) {
                                System.out.println("Entrada inválida. Por favor, insira um número inteiro.");
                                scanner.next();
                            }
                        }
                    }
                } else if (op == 2) {
                    System.out.println("Voltando ao menu principal...");
                    break;
                } else if (op == 9) {
                    break;
                } else {
                    System.out.println("Opção indisponivel. Tente novamente.");
                }
            } catch (Exception e) {
                System.out.println("Entrada inválida. Por favor, insira um número inteiro.");
                scanner.next();
            }
        }
        return op;
    }

    public static void detalharTreinoAluno (TreinoAluno treinoaluno, int id_aluno) {
        List<Treino> treinos = ViewCliente.treinosDoTreinoAluno(treinoaluno.getId());
        List<Musculo> musculos = ViewCliente.musculoListar();

        System.out.println("\n+------------------------------------------+");
        System.out.printf("| Treinos do dia %-25s |\n", treinoaluno.getData());
        System.out.println("+------------------------------------------+");

        if (treinos.isEmpty()) {
            System.out.println("| Nenhuma treino cadastrado.               |");
            System.out.println("+------------------------------------------+");
            return;
        }

        System.out.println("| Músculo           | Descrição do Treino  |");
        System.out.println("+-------------------+----------------------+");

        for (Treino t : treinos) {
            Musculo ms = null;
            for (Musculo m : musculos) {
                if (m.getId() == t.getIdMusculo()) {
                    ms = m;
                    break;
                }
            }

            if (ms != null) {
                System.out.printf("| %-17s | %-20s |\n",
                        ms.getNome(),
                        t.getDescricao());
            } else {
                System.out.printf("| Músculo não encontrado (ID: %-4d) | %-19s |\n",
                        t.getIdMusculo(),
                        t.getDescricao(),
                        "N/A");
            }
        }
    }
}