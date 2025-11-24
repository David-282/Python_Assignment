passed_student = 0
failed_student = 0
for score in range (1,16):

     score = int(input("Enter the student Score: "))

     if score < 45:
          passed_student += 1
     else:
          failed_student += 1

print(f"The number of student that failed is {failed_student}")
print(f"The number of student that passed is {passed_student}")
       
