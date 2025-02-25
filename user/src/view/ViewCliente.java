package user.src.view;

import user.src.model.*;
import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Comparator;

public class ViewCliente {
    public static Map<String, Object> login(String cpf, String senha){
        Alunos alunos = new Alunos();

        for (Aluno c : alunos.listar()){
            if (c.getCpf().equals(cpf) && c.getSenha().equals(senha)){
                Map<String, Object> autenticado = new HashMap<>();
                autenticado.put("id", c.getId());
                autenticado.put("nome", c.getNome());
                return autenticado;
            }
        }
        return null;
    }

    public static void atualizarAluno (int id_aluno, String nome, String email, String senha, String tel, String data_cadastro, String nascimento, String sexo, String cpf, String rg, String profissao, String bairro, String cep, String rua, String numero){
        Aluno novoAluno = new Aluno(id_aluno, nome, senha, email, tel, data_cadastro, nascimento, sexo, cpf, rg, profissao);
        Alunos alunos = new Alunos();
        alunos.atualizar(novoAluno);

        Enderecos enderecos = new Enderecos();

        for (Endereco e : enderecos.listar()) {
            if (e.getIdCliente() == id_aluno) {
                Endereco novoEndereco = new Endereco(e.getId(), id_aluno, bairro, cep, rua, numero);
                enderecos.atualizar(novoEndereco);
                break;
            }
        }
    }

    public static LocalDate dataParaLocalDate(String data) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        return LocalDate.parse(data, formatter);
    }

    public static List<Medicao> listarMedicoes (int id_aluno) {
        Medicoes medicoes = new Medicoes();
        List<Medicao> lista = new ArrayList<>();

        for (Medicao medicao : medicoes.listar()) {
            if (medicao.getIdCliente() == id_aluno) {
                lista.add(medicao);
            }
        }

        lista.sort((a1, a2) -> ViewCliente.dataParaLocalDate(a2.getData()).compareTo(ViewCliente.dataParaLocalDate(a1.getData())));

        return lista;
    }

    public static List<Medida> medidasDaMedicao (int id_medicao) {
        Medidas medidas = new Medidas();
        List<Medida> lista = new ArrayList<>();

        for (Medida medida : medidas.listar()) {
            if (medida.getIdMedicoes() == id_medicao) {
                lista.add(medida);
            }
        }

        return lista;
    }

    public static List<ParteCorpo> parteCorpoListar () {
        PartesCorpo partesCorpo = new PartesCorpo();

        return partesCorpo.listar();
    }

    public static Matricula buscarMatricula (int id_aluno) {
        Matriculas matriculas = new Matriculas();

        for (Matricula m : matriculas.listar()) {
            if (m.getIdCliente() == id_aluno && m.getAtiva()) {
                return m;
            }
        }
        return null;
    }

    public static List<Pagamento> pagamentosListar (int id_matricula, int id_aluno) {
        Pagamentos pagamentos = new Pagamentos();
        List<Pagamento> lista = new ArrayList<>();

        for (Pagamento pagamento : pagamentos.listar()) {
            if (pagamento.getIdCliente() == id_aluno && pagamento.getIdMatricula() == id_matricula) {
                lista.add(pagamento);
            }
        }

        lista.sort(Comparator.comparingInt(Pagamento::getId));

        return lista;
    }

    public static String statusPagamento (Pagamento pagamento) {
        LocalDate data = ViewCliente.dataParaLocalDate(pagamento.getVencimento());
        if (!pagamento.getPago() && data.isBefore(LocalDate.now())){
            return "\u001B[31mVencido\u001B[0m";
        } if (!pagamento.getPago() && data.isAfter(LocalDate.now())){
            return "\u001B[33mA pagar\u001B[0m";
        } else {
            return "\u001B[32mPago\u001B[0m";
        }
    }

    public static void pagarMensalidade (Pagamento pagamento, String data) {
        int id = pagamento.getId();
        int id_matricula = pagamento.getIdMatricula();
        int id_cliente = pagamento.getIdCliente();
        String emissao = pagamento.getEmissao();
        String vencimento = pagamento.getVencimento();
        String data_pagamento = data;
        double valor = pagamento.getValor();
        boolean pago = true;

        ViewCliente.pagamentoAtualizar(id, id_matricula, id_cliente, emissao, vencimento, data_pagamento, valor, pago);
    }

    public static void pagamentoAtualizar (int id, int id_matricula, int id_cliente, String emissao, String vencimento, String data_pagamento, double valor, boolean pago) {
        Pagamento novopagamento = new Pagamento(id, id_matricula, id_cliente, emissao, vencimento, data_pagamento, valor, pago);
        Pagamentos pagamentos = new Pagamentos();
        pagamentos.atualizar(novopagamento);
    }

    public static Aluno buscarAluno (int id_aluno) {
        Alunos alunos = new Alunos();

        for (Aluno a : alunos.listar()) {
            if (a.getId() == id_aluno) {
                return a;
            }
        }
        return null;
    }

    public static Endereco buscarEndereco (int id_aluno) {
        Enderecos enderecos = new Enderecos();

        for (Endereco e : enderecos.listar()) {
            if (e.getIdCliente() == id_aluno) {
                return e;
            }
        }
        return null;
    }

    public static List<TreinoAluno> listarTreinosAluno (int id_aluno) {
        TreinosAlunos treinosAlunos = new TreinosAlunos();
        List<TreinoAluno> lista = new ArrayList<>();

        for (TreinoAluno ta : treinosAlunos.listar()) {
            if (ta.getIdAluno() == id_aluno) {
                lista.add(ta);
            }
        }

        return lista;
    }

    public static List<Treino> treinosDoTreinoAluno (int id_treinoAluno) {
        Treinos treinos = new Treinos();
        List<Treino> lista = new ArrayList<>();

        for (Treino t : treinos.listar()) {
            if (t.getIdTreino() == id_treinoAluno) {
                lista.add(t);
            }
        }

        return lista;
    }

    public static List<Musculo> musculoListar () {
        Musculos musculos = new Musculos();

        return musculos.listar();
    }

    public static String resgatarPlano (Matricula matricula) {
        Planos planos = new Planos();

        for (Plano p : planos.listar()) {
            if (p.getId() == matricula.getPlano()) {
                return p.getNome();
            }
        }
        return "Indisponivel";
    }

    public static String resgatarStatus (int aluno_id) {
        Matricula matricula = ViewCliente.buscarMatricula(aluno_id);
        
        if (matricula == null) {
            return "Sem matricula";
        } 
        List<Pagamento> pagamentos = ViewCliente.pagamentosListar(matricula.getId(), aluno_id);
        
        if (pagamentos.isEmpty()) {
            return "Sem pagamentos";
        }
        String status = "\u001B[32mPagante\u001B[0m";
        for (Pagamento p : pagamentos) {
            if (ViewCliente.statusPagamento(p).equals("\u001B[31mVencido\u001B[0m")) {
                status = "\u001B[31mCaloteiro\u001B[0m";
                break;
            }
        }

        return status;
    }
}
