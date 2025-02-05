import java.util.HashMap;
import java.util.Map;

public class Medicao implements Inter{
    private int id;
    private int idCliente;
    private String data;

    public Medicao(int id, int idCliente, String data) {
        setId(id);
        setIdCliente(idCliente);
        setData(data);
    }

    public void setId(int id) {
        if (id < 0) {
            throw new IllegalArgumentException("O id da medicao não pode ser negativo.");
        }
        this.id = id;
    }

    public void setIdCliente(int idCliente) {
        if (idCliente < 0) {
            throw new IllegalArgumentException("O id do cliente não pode ser negativo.");
        }
        this.idCliente = idCliente;
    }

    public void setData(String data) {
        this.data = data; // DEVE FAZER VERIFICACAO
    }

    public int getId() {
        return id;
    }

    public int getIdCliente() {
        return idCliente;
    }

    public String getData() {
        return data;
    }

    public Map<String, Object> toDict() {
        Map<String, Object> dict = new HashMap<>();
        dict.put("id", this.id);
        dict.put("id_cliente", this.idCliente);
        dict.put("data", this.data);
        return dict;
    }
}
