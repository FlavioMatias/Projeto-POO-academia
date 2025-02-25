import java.util.ArrayList;
import java.util.List;

abstract class Modelo <T extends TemNome>{
    private List<T> objetos = new ArrayList<>();

    public void inserir (T obj) {
        objetos.add(obj);
    }

    public int quantidade() {
        return objetos.size();
    }

    public void funcao () {
        for (T x : objetos) {
            System.out.println(x.getNome());
        }
    }

    public abstract void imprimir();
    // public abstract String getNome(T obj);
}

// abstract class Modelo {
//     private List<Object> objetos = new ArrayList<>();

//     public void inserir(Object obj) {
//         objetos.add(obj);
//     }

//     public int quantidade() {
//         return objetos.size();
//     }

//     public void funcao (){
//         for (Object x : objetos) {
//             if (x instanceof Cliente) {
//                 Cliente cliente = (Cliente) x;
//                 System.out.println(cliente.getNome());
//             } else if (x instanceof Vampiro) {
//                 Vampiro vampiro = (Vampiro) x;
//                 System.out.println(vampiro.getNome());
//             }
//         }
//     }

//     public abstract void imprimir();
// }
