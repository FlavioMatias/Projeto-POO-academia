public class App {
    public static void main(String[] args) throws Exception {
        Cliente c = new Cliente("Icaro", 19);
        System.out.println(c);

        Clientes cl = new Clientes();
        cl.inserir(c);
        System.out.println(cl.quantidade());
        cl.imprimir();

        Vampiro m = new Vampiro("Nosferatu", 19);
        System.out.println(m);

        Vampiros mer = new Vampiros();
        mer.inserir(m);
        System.out.println(mer.quantidade());
        mer.imprimir();
    }
}
