sentinel = 0
total_miles_gallon = 0
gallon = 0
count = 0
while gallon != -1:
      if gallon==-1:
          break
      else:
          count+=1
          gallon = float(input("Enter the gallon used(0 to stop program): "))  
          miles = float(input("Enter the miles driven: "))
          miles_gallon = miles/gallon

          print(f"The miles/gallon for this tank was: {miles_gallon}")

          total_miles_gallon += miles_gallon
         
      average = total_miles_gallon/count
      print(average)
print("Thanks for your patronage")     

