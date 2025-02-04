import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.HashMap;
import java.util.Map;

public class Aluno {
    private int id;
    private String nome;
    private String email;
    private String tel;
    private String dataCadastro;
    private String nascimento;
    private String sexo;
    private String cpf;
    private String rg;
    private String profissao;

    public Aluno(int id, String nome, String email, String tel, String dataCadastro, String nascimento, String sexo, String cpf, String rg, String profissao) {
        setId(id);
        setNome(nome);
        setEmail(email);
        setTel(tel);
        setDataCadastro(dataCadastro); // verificar se está funcionando
        setNascimento(nascimento); // verificar se está funcionando
        setSexo(sexo);
        setCpf(cpf);
        setRg(rg);
        setProfissao(profissao);
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setNome(String nome) {
        if (nome == null) {
            throw new IllegalArgumentException("O nome não pode ser nulo");
        }
        if (nome.length() < 2) {
            throw new IllegalArgumentException("O nome deve ter pelo menos 2 caracteres");
        }
        if (!nome.matches("[a-zA-Z\\s]+")){
            throw new IllegalArgumentException("O nome deve conter apenas letras e espaços");
        }
        if (!Character.isUpperCase(nome.charAt(0))) {
            throw new IllegalArgumentException("O nome deve começar com uma letra maiúscula");
        }
        this.nome = nome;
    }

    public void setEmail(String email) {
        if (email == null) {
            throw new IllegalArgumentException("O email não pode ser nulo");
        }
        
        String regex = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(email);

        if (!matcher.matches()) {
            throw new IllegalArgumentException("O email é inválido. O formato correto é 'exemplo@dominio.com'.");
        }
        this.email = email;
    }

    public void setTel(String tel) {
        if (tel == null) {
            throw new IllegalArgumentException("O telefone não pode ser nulo");
        }
        String regex = "^\\(\\d{2}\\)\\s?\\d{4,5}-\\d{4}$";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(tel);

        if (!matcher.matches()) {
            throw new IllegalArgumentException("O telefone é inválido. O formato correto é (XX) XXXXX-XXXX ou (XX) XXXX-XXXX.");
        }

        this.tel = tel;
    }

    public void setDataCadastro(String dataCadastro) {
        if (dataCadastro == null) {
            throw new IllegalArgumentException("A data de cadastro não pode ser nula");
        }
        try {
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
            LocalDate date = LocalDate.parse(dataCadastro, formatter);
            this.dataCadastro = date.format(formatter);
        } catch (DateTimeParseException e) {
            throw new IllegalArgumentException("A data de cadastro é inválida. O formato correto é dd/MM/yyyy.");
        }
    }

    public void setNascimento(String nascimento) {
        if (nascimento == null) {
            throw new IllegalArgumentException("A data de nascimento não pode ser nula");
        }
        try {
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
            LocalDate date = LocalDate.parse(nascimento, formatter);
            this.nascimento = date.format(formatter);
        } catch (DateTimeParseException e) {
            throw new IllegalArgumentException("A data de nascimento é inválida. O formato correto é dd/MM/yyyy.");
        }
    }

    public void setSexo(String sexo) {
        if (sexo == null) {
            throw new IllegalArgumentException("O sexo não pode ser nulo");
        }

        sexo = sexo.toUpperCase();

        if (sexo.equals("M") || sexo.equals("F") || sexo.equals("MASCULINO") || sexo.equals("FEMININO") || sexo.equals("OUTRO")) {
            this.sexo = sexo;
        } else {
            throw new IllegalArgumentException("Sexo inválido.");
        }
    }

    public void setCpf(String cpf) {
        if (cpf == null) {
            throw new IllegalArgumentException("O cpf não pode ser nulo");
        }
        
        cpf = cpf.replaceAll("[^0-9]", "");

        if (cpf.length() != 11 || !cpf.matches("\\d+")) {
            throw new IllegalArgumentException("O cpf é inválido. O formato correto é XXX.XXX.XXX-XX.");
        }

        if (!validarCpf(cpf)) {
            throw new IllegalArgumentException("O cpf é inválido.");
        }

        this.cpf = cpf;
    }

    public void setRg(String rg) {    
        if (rg == null) {
            throw new IllegalArgumentException("O rg não pode ser nulo");
        }
        
        rg = rg.replaceAll("\\D", "");

        if (rg.length() != 9 || !rg.matches("\\d+")) {
            throw new IllegalArgumentException("O rg é inválido. O formato correto é XXX.XXX.XXX-XX.");
        }

        this.rg = rg;
    }

    public void setProfissao(String profissao) {
        if (profissao == null || profissao.length() < 2) {
            throw new IllegalArgumentException("A profissão deve ter pelo menos 2 caracteres");
        }
        this.profissao = profissao;
    }

    private boolean validarCpf(String cpf) {
        if (cpf == null || cpf.length() != 11) {
            return false;
        }

        int[] peso1 = {10, 9, 8, 7, 6, 5, 4, 3, 2};
        int digito1 = calcularDigito(cpf, peso1);

        int[] peso2 = {11, 10, 9, 8, 7, 6, 5, 4, 3, 2};
        int digito2 = calcularDigito(cpf, peso2);

        String cpfCalculado = String.format("%d%d", digito1, digito2);
        return cpf.substring(9).equals(cpfCalculado);
    }

    private int calcularDigito(String cpf, int[] peso) {
        int soma = 0;
        for (int i = 0; i < peso.length; i++) {
            soma += Character.getNumericValue(cpf.charAt(i)) * peso[i];
        }
        int resultado = 11 - (soma % 11);
        return (resultado == 10 || resultado == 11) ? 0 : resultado;
    }

    public int getId() {
        return id;
    }

    public String getNome() {
        return nome;
    }

    public String getEmail() {
        return email;
    }

    public String getTel() {
        return tel;
    }

    public String getDataCadastro() {
        return dataCadastro;
    }

    public String getNascimento() {
        return nascimento;
    }

    public String getSexo() {
        return sexo;
    }

    public String getCpf() {
        return cpf;
    }

    public String getRg() {
        return rg;
    }

    public String getProfissao() {
        return profissao;
    }

    public Map<String, Object> toDict(){
        Map<String, Object> dict = new HashMap<>();
        dict.put("id", this.id);
        dict.put("nome", this.nome);
        dict.put("email", this.email);
        dict.put("tel", this.tel);
        dict.put("data_cadastro", this.dataCadastro);
        dict.put("nascimento", this.nascimento);
        dict.put("sexo", this.sexo);
        dict.put("cpf", this.cpf);
        dict.put("rg", this.rg);
        dict.put("profissao", this.profissao);
        return dict;
    }
}