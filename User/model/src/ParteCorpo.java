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
            throw new IllegalArgumentException("O id da parte do corpo nao pode ser negativo.");
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
        String[] unidadesValidas = {"cm", "m", "kg", "mmHg", "bpm", "%"};

        if (unidade == null || unidade.trim().isEmpty()) {
            throw new IllegalArgumentException("A unidade deve ser uma string nao vazia.");
        }

        boolean unidadeValida = false;
        for (String validUnidade : unidadesValidas) {
            if (unidade.equalsIgnoreCase(validUnidade)) {
                unidadeValida = true;
                break;
            }
        }

        if (unidadeValida) {
            this.unidade = unidade;
        } else {
            throw new IllegalArgumentException("Unidade nao reconhecida.");
        }
    }

    public int getId() {
        return this.id;
    }    

    public String getNome() {  
        return this.nome;
    }

    public String getUnidade() {
        return this.unidade;
    }

    public Map<String, Object> toDict() {
        Map<String, Object> dict = new HashMap<>();
        dict.put("id", this.id);
        dict.put("nome", this.nome);
        dict.put("unidade", this.unidade);
        return dict;
    }

    @Override
    public String toString() {
        return "ParteCorpo(ID: " + this.id + ", Nome: " + this.nome + ", Unidade: " + this.unidade + ")";
    }
}
