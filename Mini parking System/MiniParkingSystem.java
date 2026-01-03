import java.util.Scanner;
import java.util.Arrays;
public class MiniParkingSystem{
//     static  Scanner input = new Scanner(System.in);
     static int lots=0;
     public static void main(String[]args){

          int parkingLot[] = new int [20];
           Scanner input = new Scanner(System.in);
          boolean condition = true;
//          int lots =0;
       while(condition){
                         System.out.println("\n");
     System.out.println("Welcome to our Mini-Parking System.");
     System.out.println("Please press 1 to park in any avaliable space");
     System.out.println("Please press 2 to remove your car from the parking lot");
     System.out.println("Please press 0 to exit the app");
     System.out.print("Input any of the options from above: ");
          int option = input.nextInt();
          input.nextLine();
               switch (option){

               case 1->{parkCar(parkingLot);
                
                         if (lots==20){
                               System.out.println("The parking spaces are filled up, check back later");
                         condition=false;
                                                 }
//                         System.out.print(Arrays.toString(parkingLot));}
                    for(int count =0; count<parkingLot.length;count++){
                         if (parkingLot[count]==0){
                         System.out.printf("Car Lot %d is free%n",(count+1));}
                         else{
                         System.out.printf("Car Lot %d is Ocupied%n",(count+1));}
}
}
               case 2 -> {     System.out.println();
                         System.out.print("what car lot did you park at: ");
                         int carLot= input.nextInt();
                         removeCar(carLot,parkingLot);
                         
                         for(int count =0; count<parkingLot.length;count++){
                         if (parkingLot[count]==0){
                         System.out.printf("Car Lot %d is free%n",(count+1));}
                         else{
                         System.out.printf("Car Lot %d is Ocupied%n",(count+1));}
}
//                         System.out.print(Arrays.toString(parkingLot));
                 
}
               case 0-> {condition=false;
                         System.out.println("Thank you for choosing us");}

               default ->{System.out.println("Oga pick from the option above abi u no fit read English well ");}
                              }
}
}

public static void  parkCar (int [] parkingLot){

     for (int count=0;count< parkingLot.length;count++){

          if(parkingLot[count]==0){
               parkingLot[count]=1;
               System.out.println("**********PARKING TICKET**********");
               System.out.println("You are parked at car lot number " + (count + 1));
               lots+=1;
               break;
}
}        
}

public static void  removeCar (int carLot, int [] parkingLot){

          if (carLot <1 ||carLot >parkingLot.length){
          System.out.println(" INVALID !!! Enter parking lot space between 1 and 20");
               return;
}
                    if (parkingLot[carLot-1]==0){
                    System.out.println("Your are not parked there");
           
}                  
          else {
               parkingLot[carLot-1]=0;
                 lots-=1;
                System.out.println("**********THANK YOU FOR PARKING WITH US**********");
               System.out.println("You have removed your car from car lot " + (carLot));               
              
}

                    
}



}
