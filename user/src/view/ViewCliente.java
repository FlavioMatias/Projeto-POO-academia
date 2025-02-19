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
}
