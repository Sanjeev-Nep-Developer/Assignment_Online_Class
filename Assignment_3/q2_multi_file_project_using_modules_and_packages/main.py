from finance_tools.tax import calculate_tax
from finance_tools.loan import calculate_emi


income = float(input("Enter your annual income : "))
tax = calculate_tax(income)
print("Tax to pay : ",tax)


principal  = float(input("Enter loan amount : "))
rate = float(input("Enter interest rate : "))
time = int(input("Enter time (years) : "))


emi = calculate_emi(principal,rate,time)
print('Monthly EMI : ',round(emi,2))
