import java.util.Scanner;
     public class Calculator{
     public static void main(String[]args){
     
     Scanner key = new Scanner(System.in);
     System.out.print("Enter the first integer: ");
     int numberOne = key.nextInt();
     System.out.print("Enter a mathematical operator to use(+,-,*,/): ");
     String operator = key.next();
     System.out.print("Enter the second integer: ");
     int numberTwo = key.nextInt();
     

     int sum = numberOne + numberTwo;
     int subtraction = numberOne - numberTwo;
     int product = numberOne * numberTwo;
     double division = numberOne/numberTwo;

    

     if (operator.equals("+"))
          {System.out.printf("The Sum of the numbers is %d",sum);}
     if (operator.equals("-"))
          {System.out.printf("subtracting the numbers will result in %d",subtraction);}
     if (operator.equals("/"))
          {System.out.printf("The Division  of the numbers is %f",division);} 
     if (operator.equals("*"))
          {System.out.printf("The Product of the numbers is %d%n",product);} 
     

    }

}
