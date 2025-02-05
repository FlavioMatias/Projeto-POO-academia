import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

public class Enderecos extends CRUD<Endereco>{
    @Override
    public void salvar(){
        try {
            FileWriter writer = new FileWriter("data/enderecos.json");
            Gson gson = new Gson();
            gson.toJson(objetos, writer);
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void abrir(){
        objetos.clear();
        try {
            FileReader reader = new FileReader("data/enderecos.json");
            Type listType = new TypeToken<List<CRUD>>(){}.getType();
            objetos = new Gson().fromJson(reader, listType);
            reader.close();
        } catch (FileNotFoundException e) {
            // pass
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
