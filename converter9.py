# convert.py
# A program to convert fahrenheit temps to Celsius
# by: Susan Computewell

def main():
    fahrenheit = eval(input("Enter the fahrenheit temperature: "))
    Celsius = 5/9 * (fahrenheit - 32) 
    print("The temperature is ",  Celsius, "  Celsius.")

main()
