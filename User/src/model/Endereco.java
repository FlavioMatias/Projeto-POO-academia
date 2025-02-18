import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.HashMap;
import java.util.Map;

public class Endereco implements Inter{
    private int id;
    private int id_cliente;
    private String bairro;
    private String cep;
    private String rua;
    private String numero;

    public Endereco(int id, int id_cliente, String bairro, String cep, String rua, String numero) {
        setId(id);
        setIdCliente(id_cliente);
        setBairro(bairro);
        setCep(cep);
        setRua(rua);
        setNumero(numero);
    }

    public void setId(int id) {
        if (id < 0) {
            throw new IllegalArgumentException("O id do endereço nao pode ser negativo.");
        }

        this.id = id;
    }

    public void setIdCliente(int id_cliente) {
        if (id_cliente < 0) {
            throw new IllegalArgumentException("ID do cliente deve ser um numero inteiro nao negativo.");
        }

        this.id_cliente = id_cliente;
    }

    public void setBairro(String bairro) {
        if (bairro == null || bairro.trim().isEmpty()) {
            throw new IllegalArgumentException("O bairro nao pode ser nulo ou vazio.");
        }

        this.bairro = bairro;
    }

    public void setCep(String cep) {
        String regex = "^(\\d{5}-\\d{3})|(\\d{8})$";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(cep);

        if (!matcher.matches()) {
            throw new IllegalArgumentException("CEP deve ter 8 digitos numericos.");
        }

        this.cep = cep;
    }

    public void setRua(String rua) {
        if (rua == null || rua.trim().isEmpty()) {
            throw new IllegalArgumentException("A rua nao pode ser vazia.");
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
            throw new IllegalArgumentException("Número deve ser numerico ou uma string valida como 'Apto. 101'.");
        }

        this.numero = numero;
    }

    public int getId() {
        return this.id;
    }

    public int getIdCliente() {
        return this.id_cliente;
    }

    public String getBairro() {
        return this.bairro;
    }

    public String getCep() {
        return this.cep;
    }

    public String getRua() {        
        return this.rua;
    }

    public String getNumero() {
        return this.numero;
    }

    public Map<String, Object> toDict() {
        Map<String, Object> dict = new HashMap<>();
        dict.put("id", this.id);
        dict.put("id_cliente", this.id_cliente);
        dict.put("bairro", this.bairro);
        dict.put("cep", this.cep);
        dict.put("rua", this.rua);
        dict.put("numero", this.numero);
        return dict;
    }

    @Override
    public String toString() {
        return "Endereco ID: " + this.id + "\n" +
                "ID do Cliente: " + this.id_cliente + "\n" +
                "Bairro: " + this.bairro + "\n" +
                "CEP: " + this.cep + "\n" +
                "Rua: " + this.rua + "\n" +
                "Numero: " + this.numero + "\n";
    }
}
