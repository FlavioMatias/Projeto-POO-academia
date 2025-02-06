import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;

public class Matricula implements Inter{
    private int id;
    private int id_cliente;
    private String plano;
    private String data;
    private String validade;

    public Matricula(int id, int id_cliente, String plano, String data, String validade) {
        setId(id);
        setIdCliente(id_cliente);
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

    public void setIdCliente(int id_cliente) {
        if (id_cliente < 0) {
            throw new IllegalArgumentException("O id do cliente não pode ser negativo.");
        }
        this.id_cliente = id_cliente;
    }

    public void setPlano(String plano) {
        if (plano == null) {
            throw new IllegalArgumentException("Plano invalido");
        }
        this.plano = plano;
    }

    public void setData(String data) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        try {
            LocalDate dateObj = LocalDate.parse(data, formatter);

            if (dateObj.isAfter(LocalDate.now())) {
                throw new IllegalArgumentException("Data nao pode ser no futuro.");
            }

            this.data = data;
        } catch (DateTimeParseException e) {
            throw new IllegalArgumentException("Data invalida. Use o formato 'DD/MM/YYYY'.");
        }
    }

    public void setValidade(String validade) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        try {
            LocalDate dateObj = LocalDate.parse(data, formatter);

            if (dateObj.isAfter(LocalDate.now())) {
                throw new IllegalArgumentException("Data de validade nao pode ser no futuro.");
            }

            this.validade = validade;
        } catch (DateTimeParseException e) {
            throw new IllegalArgumentException("Data de validade invalida. Use o formato 'DD/MM/YYYY'.");
        }
    }

    public int getId() {
        return id;
    }

    public int getIdCliente() {
        return id_cliente;
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
        dict.put("id_cliente", this.id_cliente);
        dict.put("plano", this.plano);
        dict.put("data", this.data);
        dict.put("validade", this.validade);
        return dict;
    }

    @Override
    public String toString() {    
        return "Matricula:" + "\n" +
                "  id=" + this.id + "\n" +
                "  id_cliente=" + this.id_cliente + "\n" +
                "  plano=" + this.plano + "\n" +
                "  data=" + this.data + "\n" +
                "  validade=" + this.validade + "\n";
    }
}
