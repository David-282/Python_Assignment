number = int(input("Enter a number to check if it is a prime number: "))
condition = True

for count in range(2, (number // 2) + 1):
    if (number % count == 0):
        condition = False
         

if (condition and number > 1):  
    print(f"{number} is a prime number")
else:
    print(f"{number} is a prime number")

