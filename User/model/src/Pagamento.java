import java.util.HashMap;
import java.util.Map;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;

public class Pagamento implements Inter{
    private int id;
    private int id_matricula;
    private int id_cliente;
    private String emissao;
    private String vencimento;
    private String data_pagamento;
    private double valor;
    private boolean pago;

    public Pagamento(int id, int id_matricula, int id_cliente, String emissao, String vencimento, String data_pagamento, double valor, boolean pago) {
        setId(id);
        setIdMatricula(id_matricula);
        setIdCliente(id_cliente);
        setEmissao(emissao);
        setVencimento(vencimento);
        setDataPagamento(data_pagamento);
        setValor(valor);
        setPago(pago);
    }

    public void setId(int id) {
        if (id < 0) {
            throw new IllegalArgumentException("O ID deve ser um numero inteiro positivo.");
        }
        this.id = id;
    }

    public void setIdMatricula(int id_matricula) {
        if (id_matricula < 0) {
            throw new IllegalArgumentException("O ID da matrícula deve ser um numero inteiro positivo.");
        }
        this.id_matricula = id_matricula;
    }

    public void setIdCliente(int id_cliente) {
        if (id_cliente < 0) {
            throw new IllegalArgumentException("O ID do cliente deve ser um numero inteiro positivo.");
        }
        this.id_cliente = id_cliente;
    }

    public void setEmissao(String emissao) {
        this.emissao = validarData(emissao, "emissao");
    }
    
    public void setVencimento(String vencimento) {
        String vencimento_data = validarData(vencimento, "vencimento");
        
        if (this.emissao != null) {
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
            LocalDate vencimentodate = LocalDate.parse(vencimento_data, formatter);
            LocalDate emissaoDate = LocalDate.parse(this.emissao, formatter);
            
            if (vencimentodate.isBefore(emissaoDate)) {
                throw new IllegalArgumentException("A data de vencimento nao pode ser anterior a data de emissao.");
            }
        }
        
        this.vencimento = vencimento_data;
    }
    
    public void setDataPagamento(String data_pagamento) {
        if (data_pagamento != null) {
            this.data_pagamento = null;
        } else {
            String data_pagamento_data = validarData(data_pagamento, "data_pagamento");

            if (this.emissao != null) {
                DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
                LocalDate data_pagamentodate = LocalDate.parse(data_pagamento_data, formatter);
                LocalDate emissaoDate = LocalDate.parse(this.emissao, formatter);
                
                if (data_pagamentodate.isBefore(emissaoDate)) {
                    throw new IllegalArgumentException("A data de pagamento nao pode ser anterior a data de emissao.");
                }
            }
            
            this.data_pagamento = data_pagamento_data;
        }
    }
    
    public void setValor(double valor) {
        if (valor < 0) {
            throw new IllegalArgumentException("O valor não pode ser negativo.");
        }
        this.valor = valor;
    }
    
    public void setPago(boolean pago) {
        if (!(pago == true || pago == false)) {
            throw new IllegalArgumentException("O campo 'pago' deve ser um valor booleano (true ou false).");
        }

        this.pago = pago;
    }
    
    private String validarData (String data_str, String campo){
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        try {
            LocalDate dataObj = LocalDate.parse(data_str, formatter);

            return data_str;
        } catch (DateTimeParseException e) {
            throw new IllegalArgumentException("A data de " + campo + " eh invalida. O formato correto eh dd/MM/yyyy.");
        }
    }

    public int getId() {
        return this.id;
    }

    public int getIdMatricula() {
        return this.id_matricula;        
    }

    public int getIdCliente() {
        return this.id_cliente;
    }

    public String getEmissao() {
        return this.emissao;
    }

    public String getVencimento() {
        return this.vencimento;
    }

    public String getDataPagamento() {        
        return this.data_pagamento;
    }

    public double getValor() {
        return this.valor;
    }

    public boolean getPago() {
        return this.pago;
    }

    public Map<String, Object> toDict() {
        Map<String, Object> dict = new HashMap<>();
        dict.put("id", this.id);
        dict.put("id_matricula", this.id_matricula);
        dict.put("id_cliente", this.id_cliente);
        dict.put("emissao", this.emissao);
        dict.put("vencimento", this.vencimento);
        dict.put("data_pagamento", this.data_pagamento);
        dict.put("valor", this.valor);
        dict.put("pago", this.pago);
        return dict;
    }

    @Override
    public String toString() {
    return "Pagamento(ID: " + this.id + ", Matricula: " + this.id_matricula + ", Cliente: " + this.id_cliente + ", Emissao: " + this.emissao + ", Vencimento: " + this.vencimento + ", Data Pagamento: " + this.data_pagamento + ", Valor: " + this.valor + ", Pago: " + this.pago + ")";
    }
}
