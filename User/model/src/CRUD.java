import java.util.ArrayList;
import java.util.List;

abstract class CRUD{
    public static List<CRUD> objetos = new ArrayList<>();

    public abstract int getId();
    public abstract void setId(int id);

    public static void inserir(CRUD obj){
        abrir();
        int id = 0;
        for (CRUD x : objetos){
            if (x.getId() > id){
                id = x.getId();
            }
        }

        obj.setId(id + 1);
        objetos.add(obj);
        salvar();
    }

    public static List<CRUD> listar(){
        abrir();
        return objetos;
    }

    public static CRUD listarId(int id){
        abrir();
        for (CRUD x : objetos){
            if (x.getId() == id){
                return x;
            }
        }
        return null;
    }

    public static void atualizar(CRUD obj){
        CRUD x = listarId(obj.getId());
        if (x != null){
            objetos.remove(x);
            objetos.add(obj);
            salvar();
        }
    }

    public static void excluir(CRUD obj){
        CRUD x = listarId(obj.getId());
        if (x != null){
            objetos.remove(x);
            salvar();
        }
    }

    public static void abrir(){
        // pass
    }

    public static void salvar(){
        // pass
    }
}
