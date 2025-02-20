package user.src.model;
import java.util.HashMap;
import java.util.Map;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;

public class Medicao implements Inter{
    private int id;
    private int id_cliente;
    private String data;
    private boolean ativa;

    public Medicao(int id, int id_cliente, String data, boolean ativa) {
        setId(id);
        setIdCliente(id_cliente);
        setData(data);
        setAtiva(ativa);
    }

    public void setId(int id) {
        if (id < 0) {
            throw new IllegalArgumentException("O id da medicao nao pode ser negativo.");
        }
        this.id = id;
    }

    public void setIdCliente(int id_cliente) {
        if (id_cliente < 0) {
            throw new IllegalArgumentException("O id do cliente nao pode ser negativo.");
        }
        this.id_cliente = id_cliente;
    }

    public void setData(String data) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        try {
            LocalDate dataObj = LocalDate.parse(data, formatter);

            if (dataObj.isAfter(LocalDate.now())) {
                throw new IllegalArgumentException("Data nao pode ser no futuro.");
            }

            this.data = data;
        } catch (DateTimeParseException e) {
            throw new IllegalArgumentException("A data eh invalida. O formato correto eh dd/MM/yyyy.");
        }
    }

    public void setAtiva(boolean ativa) {
        if (!(ativa == true || ativa == false)) {
            throw new IllegalArgumentException("O campo 'ativa' deve ser um valor booleano (true ou false).");
        }

        this.ativa = ativa;
    }

    public int getId() {
        return this.id;
    }

    public int getIdCliente() {
        return this.id_cliente;
    }

    public String getData() {
        return this.data;
    }

    public boolean getAtiva() {
        return this.ativa;
    }   

    public Map<String, Object> toDict() {
        Map<String, Object> dict = new HashMap<>();
        dict.put("id", this.id);
        dict.put("id_cliente", this.id_cliente);
        dict.put("data", this.data);
        dict.put("ativa", this.ativa);
        return dict;
    }

    @Override
    public String toString() {
        return "Medicao(ID: " + this.id + ", ID Cliente: " + this.id_cliente + ", Data: " + this.data + ")";
    }
}
