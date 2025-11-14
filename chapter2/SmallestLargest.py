first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third integer: "))
sum = first_number + second_number + third_number
average = sum/3
multiply = first_number * second_number * third_number

print("The product of all the integer's is "+ str(multiply))
print("Sum of the numbers "+ str(sum)) 
print("Average of number is "+ str(average))    

if (first_number > second_number and  first_number > third_number):
     print("The Largest number is "+ str(first_number))
if (second_number > third_number  and second_number > first_number):
     print("The Largest number is "+ str(second_number))
if (third_number > second_number and third_number > first_number):
     print("The Largest number is "+ str(third_number))
else:
     print("You entered the same number three times")
     
if (first_number < second_number and  first_number < third_number):
     print("The Smallest number is "+ str(first_number))
if (second_number < third_number and  second_number < first_number ):
     print("The Smallest number is  "+ str(second_number))
if (third_number < second_number and third_number < first_number):
     print("The Smallest number is "+ str(third_number))



    
   
    

     
     
     
