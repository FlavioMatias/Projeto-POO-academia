import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.HashMap;
import java.util.Map;

public class Aluno implements Inter{
    private int id;
    private String nome;
    private String email;
    private String tel;
    private String data_cadastro;
    private String nascimento;
    private String sexo;
    private String cpf;
    private String rg;
    private String profissao;
    private String senha;

    public Aluno(int id, String nome, String senha, String email, String tel, String data_cadastro, String nascimento, String sexo, String cpf, String rg, String profissao) {
        setId(id);
        setNome(nome);
        setSenha(senha);
        setEmail(email);
        setTel(tel);
        setData_cadastro(data_cadastro);
        setNascimento(nascimento);
        setSexo(sexo);
        setCpf(cpf);
        setRg(rg);
        setProfissao(profissao);
    }

    public void setId(int id) {
        if (id < 0) {
            throw new IllegalArgumentException("O id nao pode ser negativo.");
        }

        this.id = id;
    }

    public void setNome(String nome) {
        if (nome == null) {
            throw new IllegalArgumentException("O nome nao pode ser nulo");
        }
        if (nome.length() < 2) {
            throw new IllegalArgumentException("O nome deve ter pelo menos 2 caracteres");
        }
        if (!nome.matches("[a-zA-Z\\s]+")){
            throw new IllegalArgumentException("O nome deve conter apenas letras e espacos");
        }
        if (!Character.isUpperCase(nome.charAt(0))) {
            throw new IllegalArgumentException("O nome deve comecar com uma letra maiuscula");
        }

        this.nome = nome;
    }

    public void setSenha(String senha){
        if (senha == null) {
            throw new IllegalArgumentException("A senha nao pode ser nulo");
        }
        if (senha.length() < 8) {
            throw new IllegalArgumentException("A senha deve ter pelo menos 8 caracteres");
        }

        this.senha = senha;
    }

    public void setEmail(String email) {
        if (email == null) {
            throw new IllegalArgumentException("O email nao pode ser nulo");
        }
        String regex = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(email);

        if (!matcher.matches()) {
            throw new IllegalArgumentException("O email eh invalido. O formato correto eh 'exemplo@dominio.com'.");
        }

        this.email = email;
    }

    public void setTel(String tel) {
        if (tel == null || !(tel instanceof String)) {
            throw new IllegalArgumentException("Telefone deve ser uma string.");
        }

        String regex = "^\\(?([0-9]{2})\\)?\\s?[0-9]{4,5}[-]?[0-9]{4}$";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(tel);

        if (!matcher.matches()) {
            throw new IllegalArgumentException("Telefone inválido. O formato correto é (XX) XXXXX-XXXX ou (XX) XXXX-XXXX.");
        }

        int ddd = Integer.parseInt(matcher.group(1));

        int[] dddsValidos = {
            11, 12, 13, 14, 15, 16, 17, 18, 19,  // SP
            21, 22, 24,  // RJ
            27, 28,  // ES
            31, 32, 33, 34, 35, 37, 38,  // MG
            41, 42, 43, 44, 45, 46,  // PR
            47, 48, 49,  // SC
            51, 53, 54, 55,  // RS
            61,  // DF
            62, 64,  // GO
            63,  // TO
            65, 66,  // MT
            67,  // MS
            68,  // AC
            69,  // RO
            71, 73, 74, 75, 77,  // BA
            79,  // SE
            81, 87,  // PE
            82,  // AL
            83,  // PB
            84,  // RN
            85, 88,  // CE
            86, 89,  // PI
            91, 93, 94,  // PA
            92, 97,  // AM
            95,  // RR
            96,  // AP
            98, 99  // MA
        };

        boolean dddValido = false;
        for (int validDdd : dddsValidos) {
            if (ddd == validDdd) {
                dddValido = true;
                break;
            }
        }

        if (!dddValido) {
            throw new IllegalArgumentException("DDD inválido. O código de área não é válido no Brasil.");
        }

        this.tel = tel;
    }

    public void setData_cadastro(String data_cadastro) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        try {
            LocalDate dataObj = LocalDate.parse(data_cadastro, formatter);

            if (dataObj.isAfter(LocalDate.now())) {
                throw new IllegalArgumentException("Data de cadastro nao pode ser no futuro.");
            }

            this.data_cadastro = data_cadastro;
        } catch (DateTimeParseException e) {
            throw new IllegalArgumentException("A data de cadastro eh invalida. O formato correto eh dd/MM/yyyy.");
        }
    }

    public void setNascimento(String nascimento) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        try {
            LocalDate dataObj = LocalDate.parse(nascimento, formatter);

            if (dataObj.isAfter(LocalDate.now())) {
                throw new IllegalArgumentException("Data de nascimento nao pode ser no futuro.");
            }

            this.nascimento = nascimento;
        } catch (DateTimeParseException e) {
            throw new IllegalArgumentException("A data de nascimento eh invalida. O formato correto eh dd/MM/yyyy.");
        }
    }

    public void setSexo(String sexo) {
        if (sexo == null) {
            throw new IllegalArgumentException("O sexo nao pode ser nulo");
        }

        sexo = sexo.toUpperCase();

        if (sexo.equals("M") || sexo.equals("F") || sexo.equals("MASCULINO") || sexo.equals("FEMININO") || sexo.equals("OUTRO")) {
            this.sexo = sexo;
        } else {
            throw new IllegalArgumentException("Sexo invalido.");
        }
    }

    public void setCpf(String cpf) {
        if (!cpf.matches("\\d{11}") && !cpf.matches("\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}")) {
            throw new IllegalArgumentException("CPF deve estar no formato xxx.xxx.xxx-xx ou conter apenas 11 dígitos numéricos.");
        }

        cpf = cpf.replaceAll("\\D", "");

        if (cpf.length() != 11 || !cpf.matches("\\d+")) {
            throw new IllegalArgumentException("CPF deve conter 11 dígitos numéricos.");
        }

        if (!validarCpf(cpf)) {
            throw new IllegalArgumentException("CPF inválido.");
        }

        this.cpf = String.format("%s.%s.%s-%s", cpf.substring(0, 3), cpf.substring(3, 6), cpf.substring(6, 9), cpf.substring(9));
    }

    public void setRg(String rg) {    
        if (rg == null) {
            throw new IllegalArgumentException("O rg nao pode ser nulo");
        }
        
        rg = rg.replaceAll("\\D", "");

        if (rg.length() != 9 || !rg.matches("\\d+")) {
            throw new IllegalArgumentException("RG deve conter 9 digitos numericos.");
        }

        this.rg = rg;
    }

    public void setProfissao(String profissao) {
        if (profissao == null || profissao.length() < 2) {
            throw new IllegalArgumentException("profissao invalida");
        }
        this.profissao = profissao;
    }

    private boolean validarCpf(String cpf) {
        if (cpf == null || cpf.length() != 11 || cpf.equals(String.valueOf(cpf.charAt(0)).repeat(11))) {
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
        return this.id;
    }

    public String getNome() {
        return this.nome;
    }

    public String getSenha() {
        return this.senha;
    }

    public String getEmail() {
        return this.email;
    }

    public String getTel() {
        return this.tel;
    }

    public String getData_cadastro() {
        return this.data_cadastro;
    }

    public String getNascimento() {
        return this.nascimento;
    }

    public String getSexo() {
        return this.sexo;
    }

    public String getCpf() {
        return this.cpf;
    }

    public String getRg() {
        return this.rg;
    }

    public String getProfissao() {
        return this.profissao;
    }

    public Map<String, Object> toDict(){
        Map<String, Object> dict = new HashMap<>();
        dict.put("id", this.id);
        dict.put("nome", this.nome);
        dict.put("senha", this.senha);
        dict.put("email", this.email);
        dict.put("tel", this.tel);
        dict.put("data_cadastro", this.data_cadastro);
        dict.put("nascimento", this.nascimento);
        dict.put("sexo", this.sexo);
        dict.put("cpf", this.cpf);
        dict.put("rg", this.rg);
        dict.put("profissao", this.profissao);
        return dict;
    }

    @Override
    public String toString() {
        return "Aluno ID: " + this.id + "\n" +
                "Nome: " + this.nome + "\n" +
                "Email: " + this.email + "\n" +
                "Telefone: " + this.tel + "\n" +
                "Data de cadastro: " + this.data_cadastro + "\n" +
                "Data de nascimento: " + this.nascimento + "\n" +
                "Sexo: " + this.sexo + "\n" +
                "CPF: " + this.cpf + "\n" +
                "RG: " + this.rg + "\n" +
                "Profissao: " + this.profissao + "\n";
    }
}