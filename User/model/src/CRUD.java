import java.util.ArrayList;
import java.util.List;

abstract class CRUD{
    protected List<Object> objetos = new ArrayList<>();

    public void inserir(Object obj){
        abrir();
        int id = 0;
        for (Object x : objetos){
            if (x.getId() > id){
                id = x.getId();
            }
        }

        obj.setId(id + 1);
        objetos.add(obj);
        salvar();
    }

    public List<Object> listar(){
        abrir();
        return objetos;
    }

    public Object listarId(int id){
        abrir();
        for (Object x : objetos){
            if (x.getId() == id){
                return x;
            }
        }
        return null;
    }

    public void atualizar(Object obj){
        Object x = listarId(obj.getId());
        if (x != null){
            objetos.remove(x);
            objetos.add(obj);
            salvar();
        }
    }

    public void excluir(Object obj){
        Object x = listarId(obj.getId());
        if (x != null){
            objetos.remove(x);
            salvar();
        }
    }

    // public abstract int getId();
    // public abstract void setId(int id);

    public abstract void abrir();
    public abstract void salvar();
}
