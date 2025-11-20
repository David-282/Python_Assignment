score = int(input("Enter your score(1 or 2 will end the program): "))
sentinel_one = 1
sentinel_two = 2
pass_mark = 0
fail_mark = 0

while (score != sentinel_one or score != sentinel_two):
     if (score == sentinel_one or score == sentinel_two):
              
          print("End of Program")
          break
     else: 
         
          if (score >= 50):
               pass_mark+= 1
     
          if (score < 50):
               fail_mark+= 1
     score = int(input("Enter your Score(1 or 2 will end the program): "))


print(f"The amount of pass mark is {pass_mark}")
print(f"The amount of fail mark is {fail_mark}")


