import java.sql.*;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        try{

            Class.forName("org.sqlite.JDBC");
            Connection co  = DriverManager.getConnection(
                "jdbc:sqlite:APP.db");
            System.out.println("Connected");
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
        
    }
}
