investment_amount = int(input("Enter the Initial Investment: "))
years = int(input("Enter the years of years: "))
rate = float(input("Enter the interest rate: "))


for years in range(0,years):
     investment_amount += (investment_amount*(rate/100))
     print(f" {years+1}    {rate}     {investment_amount}")
     


