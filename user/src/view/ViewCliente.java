package user.src.view;

import user.src.model.*;
import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

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

    public static void atualizarAluno (int id_aluno, String nome, String email, String senha, String tel, String data_cadastro, String nascimento, String sexo, String cpf, String rg, String profissao){
        Aluno novoAluno = new Aluno(id_aluno, nome, senha, email, tel, data_cadastro, nascimento, sexo, cpf, rg, profissao);
        Alunos alunos = new Alunos();
        alunos.atualizar(novoAluno);
    }

    public static LocalDate getDataAsLocalDate(String data) {
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

        lista.sort((a1, a2) -> ViewCliente.getDataAsLocalDate(a2.getData()).compareTo(ViewCliente.getDataAsLocalDate(a1.getData())));

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
}
