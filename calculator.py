# A programe that calculate the tip
    
def main():
    print("What was the value of the bill?")
    bill = eval(input("Enter the initial value:"))
def tip():
    print("How was the service?")
    service = input()
    if service == "good":
        percentage = 0.20
    else:
        percentage = 0.15       
    tip = bill * percentage
    print(tip) 

main()
