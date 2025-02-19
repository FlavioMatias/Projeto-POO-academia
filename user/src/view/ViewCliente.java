package user.src.view;

import user.src.model.*;
import java.util.Map;
import java.util.HashMap;
import java.util.List;

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
}
