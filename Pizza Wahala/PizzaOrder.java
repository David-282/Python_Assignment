import java.util.Scanner;
     public class PizzaOrder{
     public static void main(String[]args){
     
     Scanner userInput = new Scanner(System.in);
     System.out.print("******Welcome to Scambirah Pizza joint*****");
     System.out.print(""" 
     ----------------------------------------------------              
     |  Pizza Type |  Number of Slices |  Price Per Box |
     ----------------------------------------------------
     |Sapa Size    |4                  |2,000           |
     ----------------------------------------------------
     |Small Money  |6                  |2,400           |
     ----------------------------------------------------
     |Big Boys     |8                  |3,000           |
     ----------------------------------------------------
     |Odogwu       |12                 |4,200           |
     ----------------------------------------------------


     """);
     
     int pricePerBox=1;
     int numberOfSlices=1;
     
     System.out.print("Enter the the amount of guest ypu are expecting: ");
     int guestNumber = userInput.nextInt();
     userInput.nextLine().toLowerCase();
     System.out.print("Which type of pizza would you like to get: ");
   
     String pizzaType = userInput.nextLine().toLowerCase();     
    
     if (pizzaType.equals("sapa size")){
          numberOfSlices=4;
          pricePerBox=2000;}

     else if (pizzaType.equals("small money")){
          numberOfSlices=6;
          pricePerBox=2400;}

     else if (pizzaType.equals("big boys")){
          numberOfSlices=8;
          pricePerBox=3000;}

     else if (pizzaType.equals("odogwu")){
          numberOfSlices=12;
          pricePerBox=4200;}
    
     int numberOfBoxes = (int) Math.ceil((double)guestNumber/numberOfSlices);
     int remainder=(numberOfBoxes*numberOfSlices)-guestNumber;
     int price= numberOfBoxes*pricePerBox;



     System.out.printf("%s size contain %d slice per box, %d  boxes should be sufficient for people as it would contain %d slices in all%n",pizzaType,numberOfSlices,numberOfBoxes,guestNumber,numberOfBoxes*numberOfSlices);


     System.out.printf("After Serving %d slices, you should have %d slices left%n",guestNumber,remainder);
     System.out.printf("%d =%d per box for %d boxes %n",price,pricePerBox,numberOfBoxes);













} 
}
