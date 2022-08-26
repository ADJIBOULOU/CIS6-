# convert.py
# A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    celsius = eval(input("Enter the Celsius temperature: "))
    fahrenheit = (9/5) * celsius + 32
    print("The temperature is ", fahrenheit, " Fahrenheit.")

main()
