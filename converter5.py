#converstionchart.py
#     A program to compute and print a table of Celsius temperatures and the Fahrenheit equivalents every 10 degrees
#     from 0 degrees celsius to 100 degrees celsius

def main():
    print("Celisus Temperatures and")
    print("Their Fahrenheit Equivalents")
    print("{0:<14}{1:<14}".format("C", "F"))
    print("----------------------------")
    for i in range(11):
        celsius = 10 * i
        fahrenheit = int(9/5 * celsius + 32)
        print("{0:<14}{1:<14}".format(celsius, fahrenheit))
        
main()
        # celsius = celsius + 10
