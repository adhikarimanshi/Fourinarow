import java.util.Scanner;

// Custom Exception Class
class MyException extends Exception {
    public MyException(String message) {
        super(message);
    }
}

public class BankTransaction {
    
    // Method to handle withdrawal
    public static double withdrawAmount(double balance, double withdraw) throws MyException {
        if (withdraw > balance) {
            throw new MyException("Withdrawal amount exceeds balance!");
        }
        balance -= withdraw;
        return balance;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        try {
            // Taking input for balance and withdraw amount
            System.out.print("Enter balance amount: ");
            double balance = sc.nextDouble();
            
            System.out.print("Enter withdraw amount: ");
            double withdraw = sc.nextDouble();
            
            // Try withdrawing
            double remainingBalance = withdrawAmount(balance, withdraw);
            System.out.println("Remaining balance: " + remainingBalance);
            
        } catch (MyException e) {
            // Handle custom exception
            System.out.println(e.getMessage());
        } catch (Exception e) {
            // Handle other exceptions
            System.out.println("Invalid input!");
        } finally {
            sc.close();
        }
    }
}
