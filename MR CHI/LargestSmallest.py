sentinel = 0

number = int(input("Enter a number (0 to stop): "))

if (number == sentinel):
    print("No number entered.")
else:
    largest = number
    smallest = number

    while (number != sentinel):
        number = int(input("Enter a new number (0 to stop): "))

        if (number == sentinel):
          
          if (number > largest):
            largest = number

        if (number < smallest):
            smallest = number

    print("The smallest number is", smallest)
    print("The largest number is", largest)

