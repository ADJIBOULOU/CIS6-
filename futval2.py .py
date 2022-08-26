#futval.py
#   A program to compute the value of an investment
#   carried 10 years into future

def main():
    print("This program calculates the future value of a 100-years investment.")
    
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate:" ))

    for i in range (100):
        principal = principal * (1 + apr)


    print("The value in 100 years is:", principal)

main()    
