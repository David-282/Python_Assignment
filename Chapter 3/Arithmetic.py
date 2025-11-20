
number = int(input("Enter an integer: "))
addition = number
product = number
smallest = number
largest = number 
average = 0
     
for number in range (1,4):
     number = int(input("Enter an integer: "))
     
     product *= number
     addition += number

     if  number < smallest:
          smallest = number
     if  number > largest:
          largest = number
average =  addition/4

print(f"The sum of the integers is {addition}")  
print(f"The product of the integers is {product}")  
print(f"The average of the integers i {average}")  
print(f"The smallest number is {smallest}")  
print(f"The largest number is {largest}")               

     
