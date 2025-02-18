import java.util.HashMap;
import java.util.Map;
import java.util.regex.Pattern;

public class Plano implements Inter {
    private static final Pattern TEMPO_REGEX = Pattern.compile("^\\d+\\s(ano|anos|mes|meses|semana|semanas|dia|dias)$|^(ano|anos|mes|meses|semana|semanas|dia|dias)$");

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
            throw new IllegalArgumentException("O ID deve ser um numero inteiro positivo.");
        }
        this.id = id;
    }

    public void setNome(String nome) {
        if (nome == null || nome.trim().isEmpty()) {
            throw new IllegalArgumentException("O nome do plano nao pode estar vazio.");
        }
        this.nome = nome.trim();
    }

    public void setValor(double valor) {
        if (valor < 0) {
            throw new IllegalArgumentException("O valor do plano nao pode ser negativo.");
        }
        this.valor = valor;
    }

    public void setTempo(String tempo) {
        tempo = tempo.toLowerCase().replace("mês", "mes");

        if (!TEMPO_REGEX.matcher(tempo).matches()) {
            throw new IllegalArgumentException("O tempo de duracao nao eh valido.");
        }
        this.tempo = tempo;
    }

    public int getId() {
        return this.id;
    }

    public String getNome() {
        return this.nome;
    }

    public double getValor() {
        return this.valor;
    }

    public String getTempo() {
        return this.tempo;
    }

    public Map<String, Object> toMap() {
        Map<String, Object> map = new HashMap<>();
        map.put("id", id);
        map.put("nome", nome);
        map.put("valor", valor);
        map.put("tempo", tempo);
        return map;
    }

    @Override
    public String toString() {
        return "Plano(ID: " + this.id + ", Nome: " + this.nome + ", Valor: R$" + this.valor + ", Tempo: " + this.tempo + ")";
    }
}
