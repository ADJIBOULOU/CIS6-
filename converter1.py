# convert.py
# A program to convert Celsius temps to Fahrenheit  
# by: Susan Computewell

def main():
    print("This program coverts a temperature in Celsius to a temperature in Fahrenheit.")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = (9/5) * celsius + 32    
    print("The temperature is ", fahrenheit, "fahrenheit")

main()
