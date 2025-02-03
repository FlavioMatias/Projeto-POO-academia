import java.util.HashMap;
import java.util.Map;

public class Treino {
    private int id;
    private int idMusculo;
    private int idTreino;
    private String descricao;

    public Treino(int id, int idMusculo, int idTreino, String descricao) {
        setId(id);
        setIdMusculo(idMusculo);        
        setIdTreino(idTreino);
        setDescricao(descricao);
    }

    public void setId(int id) {
        if (id < 0) {
            throw new IllegalArgumentException("O id do treino não pode ser negativo.");
        }
        this.id = id;
    }

    public void setIdMusculo(int idMusculo) {
        if (idMusculo < 0) {
            throw new IllegalArgumentException("O id do treino não pode ser negativo.");
        }
        this.idMusculo = idMusculo;
    }

    public void setIdTreino(int idTreino) {
        if (idTreino < 0) {
            throw new IllegalArgumentException("O id do treino não pode ser negativo.");
        }
        this.idTreino = idTreino;
    }

    public void setDescricao(String descricao) {
        if (descricao == null) {
            throw new IllegalArgumentException("A descricao do treino não pode ser nula.");
        }
        this.descricao = descricao;
    }

    public int getId() {
        return id;
    }

    public int getIdMusculo() {
        return idMusculo;
    }   

    public int getIdTreino() {
        return idTreino;
    }

    public String getDescricao() {
        return descricao;
    }

    public Map<String, Object> toMap() {
        Map<String, Object> map = new HashMap<>();
        map.put("id", id);
        map.put("id_musculo", idMusculo);
        map.put("id_treino", idTreino);
        map.put("descricao", descricao);
        return map;
    }
}
