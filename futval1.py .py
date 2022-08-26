#futval.py
#   A program to compute the value of an investment
#   carried 10 years into future

def main():
    print("This program calculates the future value of a n-years investment.")
    n = eval(input("How many numbers should I print? "))

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate:" ))

    for i in range (n):
        principal = principal * (1 + apr)


    print("The value in n years is:", principal)

main()    
