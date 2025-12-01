number= [5,78,34,98,33,9,12,90]
smallest_number=123456789
for count in range(len(number)):
     if number[count] < smallest_number:
          smallest_number=number[count]
print(smallest_number)
