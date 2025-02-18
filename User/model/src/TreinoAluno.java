import java.util.HashMap;
import java.util.Map;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;

public class TreinoAluno implements Inter{
    private int id;
    private int id_aluno;
    private String data;
    private boolean ativa;

    public TreinoAluno(int id, int id_aluno, String data, boolean ativa) {
        setId(id);
        setIdAluno(id_aluno);
        setData(data);
        setAtiva(ativa);
    }

    public void setId(int id) {
        if (id < 0) {
            throw new IllegalArgumentException("O ID deve ser um numero inteiro positivo.");
        }
        this.id = id;
    }

    public void setIdAluno(int id_aluno) {
        if (id_aluno < 0) {
            throw new IllegalArgumentException("O ID do aluno nao pode ser negativo.");
        }
        this.id_aluno = id_aluno;
    }

    public void setData(String data) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        try {
            LocalDate dataObj = LocalDate.parse(data, formatter);

            if (dataObj.isAfter(LocalDate.now())) {
                throw new IllegalArgumentException("Data nao pode ser no futuro.");
            }

            this.data = data;
        } catch (DateTimeParseException e) {
            throw new IllegalArgumentException("A data eh invalida. O formato correto eh dd/MM/yyyy.");
        }
    }

    public void setAtiva(boolean ativa) {
        if(!(ativa == true || ativa == false)) {
            throw new IllegalArgumentException("O campo 'ativa' deve ser um valor booleano (true ou false).");
        }

        this.ativa = ativa;
    }

    public int getId() {
        return this.id;
    }

    public int getIdAluno() {
        return this.id_aluno;
    }

    public String getData() {
        return this.data;
    }

    public boolean getAtiva() {
        return this.ativa;
    }

    public Map<String, Object> toMap() {
        Map<String, Object> map = new HashMap<>();
        map.put("id", id);
        map.put("id_aluno", id_aluno);
        map.put("data", data);
        map.put("ativa", ativa);
        return map;
    }

    @Override
    public String toString() {
        return "TreinoAluno(ID: " + this.id + ", ID Aluno: " + this.id_aluno + ", Data: " + this.data + ", Ativo: " + this.ativa + ")";
    }
}
