first_integer = int(input("Enter the First number: "))
second_integer = int(input("Enter the Second number: "))
stop = 0

sum = first_integer + second_integer
print("The addition of the two integers is", sum)

num_stop = None 
while (num_stop != stop):
    num_stop = int(input("Press any number apart from 0 to continue the operation: "))
    
    if num_stop == stop:
        print("Bye, Thanks for coming")
    else:
        first_number = int(input("Enter the First number: "))
        second_number = int(input("Enter the Second number: "))
        sum_two = first_number + second_number
        print("The addition of the two integers is", sum_two)

