sentinel = -50
positive_number = 0
negative_number = 0
zeros = 0

number = int(input("Enter a number (-50) to end the program): "))

if (number == sentinel):
    print("End of program")
else:
    while (number != sentinel):
        if (number == 0):
            zeros += 1
        if (number > 0):
            positive_number += 1
        if   (number < 0):
            negative_number += 1
        
        number = int(input("Enter a number (-50) to end the program): "))

    print(f"{zeros} zeros were entered, {positive_number} positive numbers, and {negative_number} negative numbers were entered.")

