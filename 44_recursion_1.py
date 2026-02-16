# Recursion function
def printNumber(number):
    if number>=1:
        print(number)
        printNumber(number-1) 
number = 10 
printNumber(number)