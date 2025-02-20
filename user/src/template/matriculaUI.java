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
        Scanner scanner = new Scanner(System.in);
        Matricula matricula = ViewCliente.buscarMatricula(id_aluno);
        List<Pagamento> pagamentos = ViewCliente.pagamentosListar(matricula.getId(), id_aluno);
        int op = 0;

        while (true) {
            if (matricula == null) {
                System.out.println("Matrícula não encontrada para o aluno com ID " + id_aluno + ".");
                return op;
            }

            System.out.println("\nDetalhes da Matrícula:");
            System.out.println("-----------------------------");
            System.out.println("ID: " + matricula.getId());
            System.out.println("Plano: " + matricula.getPlano());
            System.out.println("Data: " + matricula.getData());
            System.out.println("Validade: " + matricula.getValidade());
            System.out.println("Status: " + (matricula.getAtiva() ? "Ativa" : "Inativa"));
            System.out.println("-----------------------------");

            System.out.println("\nPagamentos:");
            System.out.println("-----------------------------");

            if (pagamentos.isEmpty()) {
                System.out.println("Nenhum pagamento registrado.");
            } else {
                for (Pagamento pagamento : pagamentos) {
                    System.out.println("ID: " + pagamento.getId());
                    System.out.println("Valor: " + pagamento.getValor());
                    System.out.println("Data de Emissão: " + pagamento.getEmissao());
                    System.out.println("Vencimento: " + pagamento.getVencimento());
                    System.out.println("Data de Pagamento: " + pagamento.getDataPagamento());
                    System.out.println("Status: " + (ViewCliente.statusPagamento(pagamento)));
                    System.out.println("-----------------------------");
                }
            }

            System.out.println("1 - Pagar, 2 - Voltar, 9 - Fim");
            System.out.print("Informe sua opção: ");
            op = scanner.nextInt();

            if (op == 1) {
                if (pagamentos.isEmpty()) {
                    System.out.println("Nao há pagamentos para pagar.");
                } else {
                    System.out.print("\nDigite o ID do pagamento que deseja pagar: ");
                    int id_pagamento = scanner.nextInt();

                    Pagamento pagamento_selecionado = null;
                    for (Pagamento p : pagamentos) {
                        if (p.getId() == id_pagamento) {
                            pagamento_selecionado = p;
                            break;
                        }
                    }

                    if (pagamento_selecionado != null && !pagamento_selecionado.getPago()){
                        LocalDate hoje_data = LocalDate.now();
                        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
                        String dataString = data.format(formatter);
                        ViewCliente.pagarMensalidade(pagamento_selecionado, dataString);
                    }  else {
                        System.out.println("Id indisponivel.");
                    }
                }
            } else if (op == 2) {
                System.out.println("Voltando ao menu principal...");
                break;
            }else  if (op == 9){
                break;
            } else {
                System.out.println("Opção indisponivel. Tente novamente.");
            }
        }

        return op;
    }
}