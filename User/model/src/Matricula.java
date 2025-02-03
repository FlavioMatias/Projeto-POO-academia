import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;

public class Matricula {
    private int id;
    private int idCliente;
    private String plano;
    private String data;
    private String validade;

    public Matricula(int id, int idCliente, String plano, String data, String validade) {
        setId(id);
        setIdCliente(idCliente);
        setPlano(plano);
        setData(data);
        setValidade(validade);
    }

    public void setId(int id) {
        if (id < 0) {
            throw new IllegalArgumentException("O id da matricula não pode ser negativo.");
        }
        this.id = id;
    }

    public void setIdCliente(int idCliente) {
        if (idCliente < 0) {
            throw new IllegalArgumentException("O id do cliente não pode ser negativo.");
        }
        this.idCliente = idCliente;
    }

    public void setPlano(String plano) {
        if (plano == null) {
            throw new IllegalArgumentException("O plano da matricula não pode ser nulo.");
        }
        this.plano = plano;
    }

    public void setData(String data) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        try {
            LocalDate dateObj = LocalDate.parse(data, formatter);
            this.data = data;
        } catch (DateTimeParseException e) {
            throw new IllegalArgumentException("A data de cadastro é inválida. O formato correto é dd/MM/yyyy.");
        }
    }

    public void setValidade(String validade) {
        if (validade == null) {
            throw new IllegalArgumentException("A validade da matricula não pode ser nula.");
        }
        this.validade = validade;
    }

    public int getId() {
        return id;
    }

    public int getIdCliente() {
        return idCliente;
    }

    public String getPlano() {
        return plano;
    }

    public String getData() {
        return data;
    }

    public String getValidade() {
        return validade;
    }

    public Map<String, Object> toDict() {
        Map<String, Object> dict = new HashMap<>();
        dict.put("id", this.id);
        dict.put("id_cliente", this.idCliente);
        dict.put("plano", this.plano);
        dict.put("data", this.data);
        dict.put("validade", this.validade);
        return dict;
    }
}
