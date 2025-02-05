import java.util.HashMap;
import java.util.Map;

public class ParteCorpo implements Inter{
    private int id;
    private String nome;
    private String unidade;

    public ParteCorpo(int id, String nome, String unidade) {
        setId(id);
        setNome(nome);
        setUnidade(unidade);
    }

    public void setId(int id) {
        if (id < 0) {
            throw new IllegalArgumentException("O id da parte do corpo não pode ser negativo.");
        }
        this.id = id;
    }

    public void setNome(String nome) {
        if (nome == null) {
            throw new IllegalArgumentException("O nome da parte do corpo não pode ser nulo.");
        }
        this.nome = nome;
    }

    public void setUnidade(String unidade) {
        if (unidade == null) {
            throw new IllegalArgumentException("A unidade da parte do corpo não pode ser nula.");
        }
        this.unidade = unidade;
    }

    public int getId() {
        return id;
    }    

    public String getNome() {  
        return nome;
    }

    public String getUnidade() {
        return unidade;
    }

    public Map<String, Object> toDict() {
        Map<String, Object> dict = new HashMap<>();
        dict.put("id", this.id);
        dict.put("nome", this.nome);
        dict.put("unidade", this.unidade);
        return dict;
    }
}
