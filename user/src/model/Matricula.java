package user.src.model;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;

public class Matricula implements Inter{
    private int id;
    private int id_aluno;
    private int plano;
    private String data;
    private String validade;
    private boolean ativa;

    public Matricula(int id, int id_aluno, int plano, String data, String validade, boolean ativa) {
        setId(id);
        setIdCliente(id_aluno);
        setPlano(plano);
        setData(data);
        setValidade(validade);
        setAtiva(ativa);
    }

    public void setId(int id) {
        if (id < 0) {
            throw new IllegalArgumentException("O id da matricula não pode ser negativo.");
        }
        this.id = id;
    }

    public void setIdCliente(int id_aluno) {
        if (id_aluno < 0) {
            throw new IllegalArgumentException("O id do cliente não pode ser negativo.");
        }
        this.id_aluno = id_aluno;
    }

    public void setPlano(int plano) {
        if (plano < 0) {
            throw new IllegalArgumentException("Plano invalido");
        }
        this.plano = plano;
    }

    public void setData(String data) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        try {
            LocalDate dateObj = LocalDate.parse(data, formatter);

            this.data = data;
        } catch (DateTimeParseException e) {
            throw new IllegalArgumentException("Data invalida. Use o formato 'DD/MM/YYYY'.");
        }
    }

    public void setValidade(String validade) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        try {
            LocalDate dateObj = LocalDate.parse(validade, formatter);
            this.validade = validade;
        } catch (DateTimeParseException e) {
            throw new IllegalArgumentException("Data de validade invalida. Use o formato 'DD/MM/YYYY'.");
        }
    }

    public void setAtiva(boolean ativa) {
        if (!(ativa == true || ativa == false)) {
            throw new IllegalArgumentException("O campo 'ativa' deve ser um valor booleano (true ou false).");
        }

        this.ativa = ativa;
    }

    public int getId() {
        return id;
    }

    public int getIdCliente() {
        return id_aluno;
    }

    public int getPlano() {
        return plano;
    }

    public String getData() {
        return data;
    }

    public String getValidade() {
        return validade;
    }

    public boolean getAtiva() {
        return ativa;
    }

    public Map<String, Object> toDict() {
        Map<String, Object> dict = new HashMap<>();
        dict.put("id", this.id);
        dict.put("id_aluno", this.id_aluno);
        dict.put("plano", this.plano);
        dict.put("data", this.data);
        dict.put("validade", this.validade);
        dict.put("ativa", this.ativa);
        return dict;
    }

    @Override
    public String toString() {    
        return "Matricula:" + "\n" +
                "  id=" + this.id + "\n" +
                "  id_aluno=" + this.id_aluno + "\n" +
                "  plano=" + this.plano + "\n" +
                "  data=" + this.data + "\n" +
                "  validade=" + this.validade + "\n" +
                "  ativa=" + this.ativa + "\n";
    }
}
