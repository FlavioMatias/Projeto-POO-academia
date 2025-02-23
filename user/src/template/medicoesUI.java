package user.src.template;

import user.src.view.*;
import user.src.model.*;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class medicoesUI {
    public static int main(int id_aluno) {
        Scanner scanner = new Scanner(System.in);
        List<Medicao> medicoes = ViewCliente.listarMedicoes(id_aluno);
        int op = 0;
        boolean validInput = false;
        
        while (!validInput) {
            try {
                System.out.println("\n+---------------------------------------------+");
                System.out.println("|                SUAS MEDIÇÕES                |");
                System.out.println("+---------------------------------------------+");

                if (medicoes.isEmpty()) {
                    System.out.println("| Nenhuma medição cadastrada.           |");
                } else {
                    for (Medicao medicao : medicoes) {
                        System.out.printf("| ID: %-4d | Cliente: %-4d | Data: %-10s |\n",
                            medicao.getId(), medicao.getIdCliente(), medicao.getData());
                    }
                }

                System.out.println("+---------------------------------------------+");
                System.out.println("| 1 - Detalhar                                |");
                System.out.println("| 2 - Voltar                                  |");
                System.out.println("| 9 - Fim                                     |");
                System.out.println("+---------------------------------------------+");
                System.out.print("Informe sua opção: ");
                op = scanner.nextInt();
                
                if (op == 1) {
                    boolean entradaValida = false;
                    int id_medicao = 0;

                    System.out.println("\n+----------------------------------------+");
                    System.out.println("|       DETALHAR MEDIÇÃO POR ID          |");
                    System.out.println("+----------------------------------------+");

                    while (!entradaValida) {
                        try {
                            System.out.print("| Digite o ID da medição que deseja detalhar: ");
                            id_medicao = scanner.nextInt();
                            entradaValida = true;
                        } catch (Exception e) {
                            System.out.println("Entrada inválida. Por favor, insira um número inteiro.");
                            scanner.next();
                        }
                    }

                    Medicao medicao_selecionada = null;
                    for (Medicao medicao : medicoes) {
                        if (medicao.getId() == id_medicao) {
                            medicao_selecionada = medicao;
                            break;
                        }
                    }
                    
                    if (medicao_selecionada != null) {
                        medicoesUI.detalharMedicao(medicao_selecionada, id_aluno);

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
                    } else {
                        System.out.println("+-----------------------------------------+");
                        System.out.println("|  ID indisponível. Tente novamente.      |");
                        System.out.println("+-----------------------------------------+");
                    }

                } else if (op == 2){
                    System.out.println("Voltando ao menu principal...");
                    break;
                } else  if (op == 9){
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

    public static void detalharMedicao (Medicao medicao, int id_aluno) {
        List<Medida> medidas = ViewCliente.medidasDaMedicao(medicao.getId());
        List<ParteCorpo> partesCorpo = ViewCliente.parteCorpoListar();
        
        System.out.println("\n+------------------------------------------+");
        System.out.printf("| Medidas do dia %-25s |\n", medicao.getData());
        System.out.println("+------------------------------------------+");
        

        if (medidas.isEmpty()) {
            System.out.println("| Nenhuma medida cadastrada para esta medição. |");
            System.out.println("+------------------------------------------+");
            return;
        }

        System.out.println("| Parte do Corpo       | Valor   | Unidade |");
        System.out.println("+----------------------+---------+---------+");

        for (Medida medida : medidas) {
            ParteCorpo parteCorpo = null;
            for (ParteCorpo parte : partesCorpo) {
                if (parte.getId() == medida.getIdPartCorpo()) {
                    parteCorpo = parte;
                }
            }

            if (parteCorpo != null) {
                System.out.printf("| %-20s | %-7.2f | %-7s |\n",
                        parteCorpo.getNome(),
                        medida.getValor(),
                        parteCorpo.getUnidade());
            } else {
                System.out.printf("| Parte não encontrada (ID: %-4d) | %-7.2f | %-7s |\n",
                        medida.getIdPartCorpo(),
                        medida.getValor(),
                        "N/A");
            }
        }
    }
}