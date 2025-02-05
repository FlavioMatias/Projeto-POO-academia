import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.HashMap;
import java.util.Map;

public class Endereco implements Inter{
    private int id;
    private int idCliente;
    private String bairro;
    private String cep;
    private String rua;
    private String numero;

    public Endereco(int id, int idCliente, String bairro, String cep, String rua, String numero) {
        setId(id);
        setIdCliente(idCliente);
        setBairro(bairro);
        setCep(cep);
        setRua(rua);
        setNumero(numero);
    }

    public void setId(int id) {
        if (id < 0) {
            throw new IllegalArgumentException("O id do endereço não pode ser negativo.");
        }

        this.id = id;
    }

    public void setIdCliente(int idCliente) {
        if (idCliente < 0) {
            throw new IllegalArgumentException("O id do cliente não pode ser negativo.");
        }

        this.idCliente = idCliente;
    }

    public void setBairro(String bairro) {
        if (bairro == null || bairro.trim().isEmpty()) {
            throw new IllegalArgumentException("O bairro não pode ser nulo ou vazio.");
        }

        this.bairro = bairro;
    }

    public void setCep(String cep) {
        String regex = "^\\d{8}$";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(cep);

        if (!matcher.matches()) {
            throw new IllegalArgumentException("O CEP é inválido. O formato correto é 00000000.");
        }

        this.cep = cep;
    }

    public void setRua(String rua) {
        if (rua == null || rua.trim().isEmpty()) {
            throw new IllegalArgumentException("A rua não pode ser nula ou vazia.");
        }

        this.rua = rua;
    }

    public void setNumero(String numero) {
        String regexNumerico = "^\\d+$";
        String regexAlfanumerico = "^[A-Za-z0-9\\s]+$";

        Pattern patternNumerico = Pattern.compile(regexNumerico);
        Pattern patternAlfanumerico = Pattern.compile(regexAlfanumerico);

        Matcher matcherNumerico = patternNumerico.matcher(numero);
        Matcher matcherAlfanumerico = patternAlfanumerico.matcher(numero);

        if (!matcherNumerico.matches() && !matcherAlfanumerico.matches()) {
            throw new IllegalArgumentException("Número deve ser numérico ou uma string válida como 'Apto. 101'.");
        }

        this.numero = numero;
    }

    public int getId() {
        return id;
    }

    public int getIdCliente() {
        return idCliente;
    }

    public String getBairro() {
        return bairro;
    }

    public String getCep() {
        return cep;
    }

    public String getRua() {        
        return rua;
    }

    public String getNumero() {
        return numero;
    }

    public Map<String, Object> toDict() {
        Map<String, Object> dict = new HashMap<>();
        dict.put("id", this.id);
        dict.put("id_cliente", this.idCliente);
        dict.put("bairro", this.bairro);
        dict.put("cep", this.cep);
        dict.put("rua", this.rua);
        dict.put("numero", this.numero);
        return dict;
    }
}
