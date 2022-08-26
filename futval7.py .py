# futval.py
#    A program to compute the future value of an investment
#    with number of years determined by the user

def main():
    print("This program calculates the future value")
   
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    yearlyinvestment = eval(input("Enter the fixed yearly amount to invest: "))
    years = eval(input("Enter the number of years for the investment: "))
          
    for i in range(years):
          principal = principal + yearlyinvestment
          principal = principal * (1 + apr)

    print("The value in ", years ,"years is:", principal, sep=" ")

main()

