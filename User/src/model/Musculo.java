import java.util.HashMap;
import java.util.Map;

public class Musculo implements Inter {
    private int id;
    private String nome;

    public Musculo (int id, String nome){
        setId(id);
        setNome(nome);
    }

    public void setId(int id){
        if (id < 0) {
            throw new IllegalArgumentException("O id do musculo nao pode ser negativo.");
        }

        this.id = id;
    }

    public void setNome(String nome) {
        if (nome == null) {
            throw new IllegalArgumentException("O nome do musculo nao pode ser nulo.");
        }

        this.nome = nome;
    }

    public int getId() {
        return this.id;
    }

    public String getNome() {
        return this.nome;
    }

    public Map<String, Object> toDict() {
        Map<String, Object> dict = new HashMap<>();
        dict.put("id", this.id);
        dict.put("nome", this.nome);
        return dict;
    }

    @Override
    public String toString() {
        return "Musculo(ID: " + this.id + ", Nome: " + this.nome + ")";
    }

}