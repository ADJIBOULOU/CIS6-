#average.py
#A simple program to average two exam scores

def main():
    print("This program computes the average of the two exams.")

    score1 = eval(input("Enter the first test score: "))
    score2 = eval(input("Enter the second test score: "))
    score3 = eval(input("Enter the third test score: "))

    average = (score1 + score2 + score3) / 3

    print("The average of the scores is:", average)

main()

