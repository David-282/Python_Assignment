sum = 0
for number in range (10,20000+1):
     if number % 10 ==  0:
          sum += number
     if sum > sum:
          sum = sum
print (f"The sum of all the multiples of 10 is {sum}")

