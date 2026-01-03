
parking_lot = []
for count in range (0,20):
     parking_lot.append(0)

def  parkCar (parking_lot):
             
     for count in range (0,len(parking_lot)):
          if parking_lot[count]==0:
               parking_lot[count]=1
               print("**********PARKING TICKET**********")
               print("You are parked at car lot number " ,(count + 1))
#               lots+=1
               break

def removeCar (car_lot, parkingLot):

     if car_lot <1 or car_lot >len(parking_lot):
          print(" INVALID !!! Enter parking lot space between 1 and 20")
          return
     
     if parking_lot[car_lot-1]==0:
          print("Your are not parked there")

                      
     else:
          parking_lot[car_lot-1]=0
#          lots-=1
          print("**********THANK YOU FOR PARKING WITH US**********")
          print("You have removed your car from car lot " , (car_lot))     



condition = True
while(condition):
     print("\n")
     print("Welcome to our Mini-Parking System.")
     print("Please press 1 to park in any avaliable space")
     print("Please press 2 to remove your car from the parking lot")
     print("Please press 0 to exit the app")
     option=(int(input("Input any of the options from above: ")))

     match option:

          case 1:
               parkCar(parking_lot)
               if 0 not in parking_lot:
                    print("The parking spaces are filled up, check back later")
                    condition = False
#               print(parking_lot)
               for count in range (0,len(parking_lot)):
                    if parking_lot[count] ==0:
                         print(f"Car Lot {count+1} is empty")                    
                    else:
                         print(f"Car Lot  {count+1} is occupied ")
                         

          case 2 :    
               print()
               car_lot=(int(input("what car lot did you park at: ")))
               removeCar(car_lot,parking_lot)
#               print(parking_lot)
               for count in range (0,len(parking_lot)):
                    if parking_lot[count]  ==0:
                         print(f"Car Lot {count+1} is empty")                    
                    else:
                         print(f"Car Lot  {count+1} is occupied ")
                         

          case 0: 
               condition=False
               print("Thank you for choosing us")
     
          case _ : 
               print("Oga pick from the option above abi u no fit read English well ")


               


