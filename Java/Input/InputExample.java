
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class InputExample {

    public static void main(String[] args){
    

    // created object bufferedreader to read input from the console
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    
    // prompt the user to enter some input
    System.out.println("Enter you Name");
    
    // Read a line of text from the console 

    String name = reader.readLine();

    // Read a line from console and convert into integer.

    int age = Integer.parseInt(reader.readLine());

    System.out.println(name + age);



     






    }
    
}
