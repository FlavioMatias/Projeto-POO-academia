import java.util.HashMap;
import java.util.Map;

public class Medida implements Inter{
    private int id;
    private int idMedicoes;
    private int idPartCorpo;
    private double valor;

    public Medida(int id, int idMedicoes, int idPartCorpo, double valor) {
        setId(id);
        setIdMedicoes(idMedicoes);
        setIdPartCorpo(idPartCorpo);
        setValor(valor);
    }

    public void setId(int id) {
        if (id < 0) {
            throw new IllegalArgumentException("O id da medicao não pode ser negativo.");
        }
        this.id = id;
    }

    public void setIdMedicoes(int idMedicoes) {
        if (idMedicoes < 0) {
            throw new IllegalArgumentException("O id da medicao não pode ser negativo.");
        }
        this.idMedicoes = idMedicoes;
    }

    public void setIdPartCorpo(int idPartCorpo) {
        if (idPartCorpo < 0) {
            throw new IllegalArgumentException("O id da medicao não pode ser negativo.");
        }
        this.idPartCorpo = idPartCorpo;
    }

    public void setValor(double valor) {
        if (valor < 0) {
            throw new IllegalArgumentException("O valor da medicao não pode ser negativo.");
        }
        this.valor = valor; // FAZER MAIS VALIDACOES
    }

    public int getId() {
        return id;
    }

    public int getIdMedicoes () {
        return idMedicoes;
    }

    public int getIdPartCorpo () {
        return idPartCorpo;
    }

    public double getValor () {
        return valor;
    }

    public Map<String, Object> toMap() {
        Map<String, Object> map = new HashMap<>();
        map.put("id", id);
        map.put("id_medicoes", idMedicoes);
        map.put("id_partCorpo", idPartCorpo);
        map.put("valor", valor);
        return map;
    }
}
