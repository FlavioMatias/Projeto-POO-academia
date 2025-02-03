import java.util.HashMap;
import java.util.Map;

public class Plano {
    private int id;
    private String nome;
    private double valor;
    private String tempo;

    public Plano(int id, String nome, double valor, String tempo) {
        setId(id);
        setNome(nome);
        setValor(valor);
        setTempo(tempo);
    }

    public void setId(int id) {
        if (id < 0) {
            throw new IllegalArgumentException("O id do plano não pode ser negativo.");
        }
        this.id = id;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setValor(double valor) {
        if (valor < 0) {
            throw new IllegalArgumentException("O valor do plano não pode ser negativo.");
        }
        this.valor = valor;
    }

    public void setTempo(String tempo) {
        this.tempo = tempo;
    }

    public int getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public double getValor() {
        return valor;
    }

    public String getTempo() {
        return tempo;
    }

    public Map<String, Object> toMap() {
        Map<String, Object> map = new HashMap<>();
        map.put("id", id);
        map.put("nome", nome);
        map.put("valor", valor);
        map.put("tempo", tempo);
        return map;
    }
}
