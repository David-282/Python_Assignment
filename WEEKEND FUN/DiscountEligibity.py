total_bill = int(input("Enter the Total Bill: "))
is_member = input("Are you a Member? (Yes/No): ").lower()

membership = (is_member == "yes")
print (membership)

if (total_bill >= 1000 and membership):
     print("You are Eligible for 10% off the Total Bill")
elif (total_bill >= 1000 and not membership):
     print("You are Eligible for 5% off the Total Bill")
else: 
     print(f"Your bill {total_bill} as not changed,as you are not eligible for any discount")




