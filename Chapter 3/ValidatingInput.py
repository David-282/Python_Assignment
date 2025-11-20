score = int(input("Enter your score: "))
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
     score = int(input("Enter your Score: "))


print(f"The amount of pass markk is {pass_mark}")
print(f"The amount of fail markk is {fail_mark}")


