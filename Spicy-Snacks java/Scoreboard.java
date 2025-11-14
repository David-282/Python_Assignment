import java.util.Scanner;
     public class Scoreboard{
     public static void main(String[]args){
     
     Scanner input = new Scanner(System.in);
     System.out.print("Enter the first score: ");
     int scoreOne = input.nextInt();
     System.out.print("Enter the second score: ");
     int scoreTwo = input.nextInt();
     System.out.print("Enter the third score: ");
     int scoreThree = input.nextInt();
          

     int sum = scoreOne + scoreTwo + scoreThree;
     double average = sum/3;

     System.out.println("The Average of the scores is  "+average);

     if(average >= 90)
     {System.out.println("The average score of the result is  A");}

     if(average >= 80)
     {System.out.println("The average score of the result is B");}

     if(average >=70)
     {System.out.println("The average score of the result is c");}

     if(average >= 60)
     {System.out.println("The average score of the result is D");}
     
     if(average < 60)
     {System.out.println("The average score of the result is F");}


}
}
   
