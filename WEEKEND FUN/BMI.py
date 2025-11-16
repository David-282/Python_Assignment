weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = weight / (height ** 2) 

if (bmi < 18.5):
     print(f"Your BMI is {bmi}.You are Underweight, Eat more")
if (bmi >= 18.5 and bmi <= 24.9):
     print(f"Your BMI is {bmi}.You are Normal, Keep it up")
if (bmi > 24.9 and bmi<= 29.9):
     print(f"Your BMI is {bmi}.You are Overwieght, Work on it Now !!!")
if (bmi > 30):
     print(f"Your BMI is {bmi}.You are Obese")
