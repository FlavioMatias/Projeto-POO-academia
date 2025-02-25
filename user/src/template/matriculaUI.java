package user.src.template;

import user.src.view.*;
import user.src.model.*;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class matriculaUI {
    public static int main(int id_aluno) {
        Matricula matricula = ViewCliente.buscarMatricula(id_aluno);
        Scanner scanner = new Scanner(System.in);
        System.out.println("oi2");
        int op = 0;
        
        while (true) {
            
            if (matricula == null) {
                System.out.println("\n+---------------------------------------------------+");
                System.out.printf("| Matrícula não encontrada para o aluno com ID %-4d |\n", id_aluno);
                System.out.println("+---------------------------------------------------+");
                return op;
            }
            List<Pagamento> pagamentos = ViewCliente.pagamentosListar(matricula.getId(), id_aluno);
            
            System.out.println("\n+-----------------------------------------+");
            System.out.println("|          DETALHES DA MATRÍCULA          |");
            System.out.println("+-----------------------------------------+");
            System.out.printf("| ID: %-12d | Plano: %-13s |\n", matricula.getId(), ViewCliente.resgatarPlano(matricula));
            System.out.printf("| Data: %-10s | Validade: %-10s |\n", matricula.getData(), matricula.getValidade());
            System.out.printf("| Status: %-31s |\n", matricula.getAtiva() ? "Ativa" : "Inativa");
            System.out.println("+-----------------------------------------+");

            System.out.println("\n+----------------------------------------------+");
            System.out.println("|                PAGAMENTOS                    |");
            System.out.println("+----------------------------------------------+");

            if (pagamentos.isEmpty()) {
                System.out.println("| Nenhum pagamento registrado.                 |");
            } else {
                for (Pagamento pagamento : pagamentos) {
                    System.out.printf("| ID: %-4d | Valor: %-8.2f | Status: %-7s |\n",
                            pagamento.getId(),
                            pagamento.getValor(),
                            ViewCliente.statusPagamento(pagamento));
                    System.out.printf("| Emissão: %-10s | Vencimento: %-10s |\n",
                            pagamento.getEmissao(),
                            pagamento.getVencimento());
                    System.out.printf("| Data de Pagamento: %-25s |\n",
                            pagamento.getDataPagamento() != null ? pagamento.getDataPagamento() : "Pendente");
                    System.out.println("+----------------------------------------------+");
                }
            }

            
            System.out.println("\n+----------------------------------------+");
            System.out.println("| 1 - Pagar                              |");
            System.out.println("| 2 - Voltar                             |");
            System.out.println("| 9 - Fim                                |");
            System.out.println("+----------------------------------------+");
            
            try{
                System.out.print("Informe sua opção: ");
                op = scanner.nextInt();

                if (op == 1) {
                    matriculaUI.pagarPagamento(pagamentos, scanner);
                } else if (op == 2) {
                    System.out.println("Voltando ao menu principal...");
                    break;
                }else  if (op == 9){
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

    public static void pagarPagamento (List<Pagamento> pagamentos, Scanner scanner) {
        if (pagamentos.isEmpty()) {
            System.out.println("\n+----------------------------------------+");
            System.out.println("|  Não há pagamentos para pagar.         |");
            System.out.println("+----------------------------------------+");
            return;
        }

        boolean entradaValida = false;
        int id_pagamento = 0;

        while (!entradaValida) {
            try {
                System.out.print("\nDigite o ID do pagamento que deseja pagar: ");
                id_pagamento = scanner.nextInt();
                entradaValida = true;
            } catch (Exception e) {
                System.out.println("Entrada inválida. Por favor, insira um número inteiro.");
                scanner.next();
            }
        }

        Pagamento pagamento_selecionado = null;
        for (Pagamento p : pagamentos) {
            if (p.getId() == id_pagamento) {
                pagamento_selecionado = p;
                break;
            }
        }

        if (pagamento_selecionado != null && !pagamento_selecionado.getPago()) {
            LocalDate hoje_data = LocalDate.now();
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
            String dataString = hoje_data.format(formatter);
            ViewCliente.pagarMensalidade(pagamento_selecionado, dataString);
        } else {
            System.out.println("\n+----------------------------------------+");
            System.out.println("|  ID indisponível ou pagamento já pago. |");
            System.out.println("+----------------------------------------+");
        }
    }
}