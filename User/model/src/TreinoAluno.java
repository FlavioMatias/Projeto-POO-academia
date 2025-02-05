import java.util.HashMap;
import java.util.Map;

public class TreinoAluno implements Inter{
    private int id;
    private int idAluno;
    private String data;
    private String dataFinal;

    public TreinoAluno(int id, int idAluno, String data, String dataFinal) {
        setId(id);
        setIdAluno(idAluno);
        setData(data);
        setDataFinal(dataFinal);
    }

    public void setId(int id) {
        if (id > 0) {
            this.id = id;
        }
    }

    public void setIdAluno(int idAluno) {
        if (idAluno > 0) {
            this.idAluno = idAluno;
        }
    }

    public void setData(String data) {
        this.data = data;
    }

    public void setDataFinal(String dataFinal) {
        this.dataFinal = dataFinal;
    }

    public int getId() {
        return id;
    }

    public int getIdAluno() {
        return idAluno;
    }

    public String getData() {
        return data;
    }

    public String getDataFinal() {
        return dataFinal;
    }

    public Map<String, Object> toMap() {
        Map<String, Object> map = new HashMap<>();
        map.put("id", id);
        map.put("id_aluno", idAluno);
        map.put("data", data);
        map.put("data_final", dataFinal);
        return map;
    }
}
