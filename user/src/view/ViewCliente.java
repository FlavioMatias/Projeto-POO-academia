package user.src.view;
import user.src.model.*;
public class ViewCliente {
    public static void login(){
        Alunos alunos = new Alunos();

        for (Aluno c : alunos.listar()){
            System.out.println(c);
        }
    }
}
