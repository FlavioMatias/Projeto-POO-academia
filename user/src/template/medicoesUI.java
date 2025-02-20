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
        
        while (true) {
            System.out.println("\nSuas medições:");

            if (medicoes.isEmpty()) {
                System.out.println("Nenhuma medição cadastrada.");
            } else {
                for (Medicao medicao : medicoes) {
                    System.out.println("- " + medicao);
                }

            }

            System.out.println("1 - Detalhar, 2 - Voltar, 9 - Fim");
            System.out.print("Informe sua opção: ");
            op = scanner.nextInt();
            
            if (op == 1) {
                if (medicoes.isEmpty()) {
                    System.out.println("Nao ha medicoes para detalhar.");
                } else {
                    System.out.print("\nDigite o ID da medição que deseja detalhar: ");
                    int id_medicao = scanner.nextInt();

                    Medicao medicao_selecionada = null;
                    for (Medicao medicao : medicoes) {
                        if (medicao.getId() == id_medicao) {
                            medicao_selecionada = medicao;
                            break;
                        }
                    }
                    
                    if (medicao_selecionada != null) {
                        medicoesUI.detalharMedicao(medicao_selecionada, id_aluno);
                    } else {
                        System.out.println("ID indisponivel.");
                    }

                }
            } else if (op == 2){
                System.out.println("Voltando ao menu principal...");
                break;
            } else  if (op == 9){
                break;
            } else {
                System.out.println("Opção indisponivel. Tente novamente.");
            }
        }

        return op;
    }

    public static void detalharMedicao (Medicao medicao, int id_aluno) {
        System.out.println("\nMedidas do dia " + medicao.getData());
        System.out.println("----------------------------------------");
        
        List<Medida> medidas = ViewCliente.medidasDaMedicao(medicao.getId());
        List<ParteCorpo> partesCorpo = ViewCliente.parteCorpoListar();

        if (medidas.isEmpty()) {
            System.out.println("Nenhuma medida cadastrada para esta medição.");
            return;
        }

        System.out.println("Parte do Corpo\t\tValor\t\tUnidade");
        System.out.println("----------------------------------------");

        for (Medida medida : medidas) {
            ParteCorpo parteCorpo = null;
            for (ParteCorpo parte : partesCorpo) {
                if (parte.getId() == medida.getIdPartCorpo()) {
                    parteCorpo = parte;
                }
            }

            if (parteCorpo != null) {
                System.out.printf("%-20s\t%.2f\t\t%s%n",
                        parteCorpo.getNome(),
                        medida.getValor(),
                        parteCorpo.getUnidade());
            } else {
                System.out.printf("Parte do corpo não encontrada (ID: %d)\t%.2f\t\t%s%n",
                        medida.getIdPartCorpo(),
                        medida.getValor(),
                        "N/A");
            }
        }
    }
}