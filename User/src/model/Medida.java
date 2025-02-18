import java.util.HashMap;
import java.util.Map;

public class Medida implements Inter{
    private int id;
    private int id_medicoes;
    private int id_partcorpo;
    private double valor;

    public Medida(int id, int id_medicoes, int id_partcorpo, double valor) {
        setId(id);
        setIdMedicoes(id_medicoes);
        setIdPartCorpo(id_partcorpo);
        setValor(valor);
    }

    public void setId(int id) {
        if (id < 0) {
            throw new IllegalArgumentException("O id nao pode ser negativo.");
        }
        this.id = id;
    }

    public void setIdMedicoes(int id_medicoes) {
        if (id_medicoes < 0) {
            throw new IllegalArgumentException("O id da medicao nao pode ser negativo.");
        }
        this.id_medicoes = id_medicoes;
    }

    public void setIdPartCorpo(int id_partcorpo) {
        if (id_partcorpo < 0) {
            throw new IllegalArgumentException("O id da parte do corpo nao pode ser negativo.");
        }
        this.id_partcorpo = id_partcorpo;
    }

    public void setValor(double valor) {
        if (valor < 0) {
            throw new IllegalArgumentException("O valor deve ser um numero positivo.");
        }
        this.valor = valor; // FAZER MAIS VALIDACOES
    }

    public int getId() {
        return this.id;
    }

    public int getIdMedicoes () {
        return this.id_medicoes;
    }

    public int getIdPartCorpo () {
        return this.id_partcorpo;
    }

    public double getValor () {
        return this.valor;
    }

    public Map<String, Object> toMap() {
        Map<String, Object> map = new HashMap<>();
        map.put("id", id);
        map.put("id_medicoes", id_medicoes);
        map.put("id_partCorpo", id_partcorpo);
        map.put("valor", valor);
        return map;
    }

    @Override
    public String toString() {
        return "Medida(ID: " + this.id + ", Medicao: " + this.id_medicoes + ", Parte Corpo: " + this.id_partcorpo + ", Valor: " + this.valor + ")";

    }
}
