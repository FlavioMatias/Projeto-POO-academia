import java.util.HashMap;
import java.util.Map;

public class Treino implements Inter{
    private int id;
    private int id_musculo;
    private int id_treino;
    private String descricao;

    public Treino(int id, int id_musculo, int id_treino, String descricao) {
        setId(id);
        setIdMusculo(id_musculo);        
        setIdTreino(id_treino);
        setDescricao(descricao);
    }

    public void setId(int id) {
        if (id < 0) {
            throw new IllegalArgumentException("O id do treino não pode ser negativo.");
        }
        this.id = id;
    }

    public void setIdMusculo(int id_musculo) {
        if (id_musculo < 0) {
            throw new IllegalArgumentException("O id do treino não pode ser negativo.");
        }
        this.id_musculo = id_musculo;
    }

    public void setIdTreino(int id_treino) {
        if (id_treino < 0) {
            throw new IllegalArgumentException("O id do treino não pode ser negativo.");
        }
        this.id_treino = id_treino;
    }

    public void setDescricao(String descricao) {
        if (descricao == null || descricao.trim().isEmpty()) {
            throw new IllegalArgumentException("A descrição não pode estar vazia.");
        }
        this.descricao = descricao.trim();
    }

    public int getId() {
        return id;
    }

    public int getIdMusculo() {
        return id_musculo;
    }   

    public int getIdTreino() {
        return id_treino;
    }

    public String getDescricao() {
        return descricao;
    }

    public Map<String, Object> toMap() {
        Map<String, Object> map = new HashMap<>();
        map.put("id", id);
        map.put("id_musculo", id_musculo);
        map.put("id_treino", id_treino);
        map.put("descricao", descricao);
        return map;
    }

    @Override
    public String toString() {
        return "Treino(" + "id=" + id + ", id_musculo=" + id_musculo + ", id_treino=" + id_treino + ", descricao=" + descricao + ')';
    }
}
