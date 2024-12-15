#!/usr/bin/env python3


interest_rate = 0.05

try:
    income = float(input("Enter your monthly income: "))
    expenses = float(input("Enter your total monthly expenses: "))

   
    monthly_savings = income - expenses

    
    annual_savings = monthly_savings * 12
    projected_savings = annual_savings + (annual_savings * interest_rate)

  
    print(f"Your monthly savings are: ${monthly_savings:.2f}")
    print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}")

except ValueError:
    print("Please enter valid numerical values for income and expenses.")

