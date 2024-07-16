import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class InputEx {

    public static void main(String[] args) {
        // Create a BufferedReader object to read input from the console
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        try {
            // Prompt the user to enter some input
            System.out.print("Enter your name: ");
            // Read a line of text from the console
            String name = reader.readLine();

            // Prompt the user to enter an integer
            System.out.print("Enter your age: ");
            // Read a line of text from the console and convert it to an integer
            int age = Integer.parseInt(reader.readLine());

            // Display the input back to the user
            System.out.println("Hello, " + name + "! You are " + age + " years old.");
        } catch (IOException e) {
            // Handle potential IOExceptions
            System.out.println("An error occurred while reading input: " + e.getMessage());
        } catch (NumberFormatException e) {
            // Handle potential NumberFormatExceptions
            System.out.println("Invalid input. Please enter a valid number for age.");
        }
    }
}
