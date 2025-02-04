import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class Main {
    public static void main(String[] args) {
        int id = 1;
        String name = "John Doe";
        String email = "r1GfB@example.com";
        String tel = "(12) 3456-7890";

        LocalDate dataCadastro = LocalDate.now();
        LocalDate nascimento = LocalDate.of(1990, 1, 1);

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        String dataCadastroStr = dataCadastro.format(formatter);
        String nascimentoStr = nascimento.format(formatter);

        String sexo = "M";
        String cpf = "713.280.564-90";
        String rg = "123456789";
        String profissao = "Programador";

        Aluno aluno = new Aluno(id, name, email, tel, dataCadastroStr, nascimentoStr, sexo, cpf, rg, profissao);

        System.out.println(aluno.toDict());

        Alunos alunos = new Alunos();
        alunos.inserir(aluno);
    }
}
