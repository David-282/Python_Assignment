number= [5,78,34,98,33,9,12,90]
largest_number=0
for count in range(len(number)):
     if number[count] > largest_number:
          largest_number=number[count]
print(largest_number)
