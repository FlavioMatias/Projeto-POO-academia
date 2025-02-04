import java.util.ArrayList;
import java.util.List;

abstract class Modelo {
    private List<Object> objetos = new ArrayList<>();

    public void inserir(Object obj) {
        objetos.add(obj);
    }

    public int quantidade() {
        return objetos.size();
    }

    public void funcao (){
        for (Object x : objetos) {
            if (x instanceof Cliente) {
                Cliente cliente = (Cliente) x;
                System.out.println(cliente.getNome());
            } else if (x instanceof Merda) {
                Merda merda = (Merda) x;
                System.out.println(merda.getNome());
            }
        }
    }

    public abstract void imprimir();
}
