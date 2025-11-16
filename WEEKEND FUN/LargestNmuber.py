first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number =int(input("Finally enter the third number: "))


largest_num = first_number

if (second_number > largest_num):
     largest_num = second_number 
if (third_number > largest_num):
     largest_num = third_number
print (f"{largest_num} is the Largest Number")
