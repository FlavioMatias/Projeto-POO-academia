public class Vampiro implements TemNome{
    private String nome;
    private int tamanho;

    public Vampiro(String nome, int tamanho) {
        this.nome = nome;
        this.tamanho = tamanho;
    }

    public String getNome() {
        return this.nome;
    }

    public String toString() {
        return this.nome + " - " + this.tamanho;
    }
}
