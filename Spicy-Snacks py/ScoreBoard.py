score_one = int(input("Enter the first score: "))
score_two = int(input("Enter the second score: "))
score_three = int(input("Enter the third score: "))

sum = score_one + score_two + score_three
average = sum/3

print("The Average of the scores is ",average)

if(average >= 100 and average <= 90):
     print("The average score of the result is  A")
if(average > 90 and average <= 80):
     print("The average score of the result is B")
if(average >=70 and average < 80):
     print("The average score of the result is c")
if(average >= 60 and average < 70):
     print("The average score of the result is D")
if(average >= 0 and average < 60):
     print("The average score of the result is F")
   
