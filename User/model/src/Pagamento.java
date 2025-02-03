import java.util.HashMap;
import java.util.Map;

public class Pagamento {
    private int id;
    private int idMatricula;
    private int idCliente;
    private String emissao;
    private String vencimento;
    private String dataPagamento;
    private double valor;
    private boolean pago;

    public Pagamento(int id, int idMatricula, int idCliente, String emissao, String vencimento, String dataPagamento, double valor, boolean pago) {
        setId(id);
        setIdMatricula(idMatricula);
        setIdCliente(idCliente);
        setEmissao(emissao);
        setVencimento(vencimento);
        setDataPagamento(dataPagamento);
        setValor(valor);
        setPago(pago);
    }

    public void setId(int id) {
        if (id < 0) {
            throw new IllegalArgumentException("O id não pode ser negativo.");
        }
        this.id = id;
    }

    public void setIdMatricula(int idMatricula) {
        if (idMatricula < 0) {
            throw new IllegalArgumentException("O id da matricula não pode ser negativo.");
        }
        this.idMatricula = idMatricula;
    }

    public void setIdCliente(int idCliente) {
        if (idCliente < 0) {
            throw new IllegalArgumentException("O id do cliente não pode ser negativo.");
        }
        this.idCliente = idCliente;
    }

    public void setEmissao(String emissao) {
        this.emissao = emissao;
    }

    public void setVencimento(String vencimento) {
        this.vencimento = vencimento;
    }

    public void setDataPagamento(String dataPagamento) {
        this.dataPagamento = dataPagamento;
    }

    public void setValor(double valor) {
        if (valor < 0) {
            throw new IllegalArgumentException("O valor não pode ser negativo.");
        }
        this.valor = valor;
    }

    public void setPago(boolean pago) {
        this.pago = pago;
    }

    public int getId() {
        return id;
    }

    public int getIdMatricula() {
        return idMatricula;        
    }

    public int getIdCliente() {
        return idCliente;
    }

    public String getEmissao() {
        return emissao;
    }

    public String getVencimento() {
        return vencimento;
    }

    public String getDataPagamento() {        
        return dataPagamento;
    }

    public double getValor() {
        return valor;
    }

    public boolean getPago() {
        return pago;
    }

    public Map<String, Object> toDict() {
        Map<String, Object> dict = new HashMap<>();
        dict.put("id", this.id);
        dict.put("id_matricula", this.idMatricula);
        dict.put("id_cliente", this.idCliente);
        dict.put("emissao", this.emissao);
        dict.put("vencimento", this.vencimento);
        dict.put("data_pagamento", this.dataPagamento);
        dict.put("valor", this.valor);
        dict.put("pago", this.pago);
        return dict;
    }
}
