import random

random_number = random.randint(0, 10)

digits = int(input("Enter any number between 0 and 10 to guess the random number: "))

while digits != random_number:
    print("Not correct")
    digits = int(input())

    if digits > random_number:
        print("Too high, try again")
    elif digits < random_number:
        print("Too low, try again")

print("The number is correct, it is", random_number)

