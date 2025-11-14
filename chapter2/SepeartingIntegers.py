number = int(input("Input the number to be rearranged: "))
if (number < 10000 or number > 99999):
     print("Digts doesn't match the required numbers")
else :
          num_one = number//10000
          num_two = (number//1000)%10
          num_three = (number//100)%10
          num_four = (number//10)%10
          num_five = number%10
          print("Reversed Number is:"  +str(num_five) + "  " +str(num_four)+ "   "+ str(num_three)+"   "+str(num_two)+"   "+ str(num_one))

