import java.util.HashMap;
import java.util.Map;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;

public class TreinoAluno implements Inter{
    private int id;
    private int id_aluno;
    private String data;
    private String data_final;

    public TreinoAluno(int id, int id_aluno, String data, String data_final) {
        setId(id);
        setIdAluno(id_aluno);
        setData(data);
        setDataFinal(data_final);
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

    public void setDataFinal(String data_final) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        try {
            LocalDate dataObj = LocalDate.parse(data_final, formatter);

            if (dataObj.isAfter(LocalDate.now())) {
                throw new IllegalArgumentException("Data final nao pode ser no futuro.");
            }

            if (dataObj.isBefore(LocalDate.parse(data, formatter))) {
                throw new IllegalArgumentException("A data final nao pode ser anterior a data de inicio.");
            }

            this.data_final = data_final;
        } catch (DateTimeParseException e) {
            throw new IllegalArgumentException("A data final eh invalida. O formato correto eh dd/MM/yyyy.");
        }
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

    public String getDataFinal() {
        return this.data_final;
    }

    public Map<String, Object> toMap() {
        Map<String, Object> map = new HashMap<>();
        map.put("id", id);
        map.put("id_aluno", id_aluno);
        map.put("data", data);
        map.put("data_final", data_final);
        return map;
    }

    @Override
    public String toString() {
        return "TreinoAluno(ID: " + this.id + ", ID Aluno: " + this.id_aluno + ", Data: " + this.data + ", Data Final: " + this.data_final + ")";
    }
}
