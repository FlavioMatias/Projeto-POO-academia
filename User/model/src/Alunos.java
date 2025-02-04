import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

public class Alunos extends CRUD{
    // acho que aplicar polimorfismo na lista de objetos possa ser util(mas tbm possa ta falando besteira) 'protected List<Aluno> objetos = new ArrayList<>();'
    @Override
    public void salvar(){
        try {
            FileWriter writer = new FileWriter("data/alunos.json");
            Gson gson = new Gson();
            gson.toJson(objetos, writer);
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void abrir(){
        objetos.clear();
        try {
            FileReader reader = new FileReader("data/alunos.json");
            Type listType = new TypeToken<List<CRUD>>(){}.getType(); // acho que é aluno ali dentro de nao crud
            objetos = new Gson().fromJson(reader, listType);
            reader.close();
        } catch (FileNotFoundException e) {
            // pass
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
