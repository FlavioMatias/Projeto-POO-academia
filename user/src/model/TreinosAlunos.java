package user.src.model;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

public class TreinosAlunos extends CRUD<TreinoAluno>{

    @Override
    public void salvar(){
        try {
            FileWriter writer = new FileWriter("Data/treinoaluno.json");
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
            FileReader reader = new FileReader("Data/treinoaluno.json");
            Type listType = new TypeToken<List<TreinoAluno>>(){}.getType();
            objetos = new Gson().fromJson(reader, listType);
            reader.close();
        } catch (FileNotFoundException e) {
            // pass
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
