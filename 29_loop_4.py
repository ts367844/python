# Docstring for 27_loop_4
# write a program to figure out whether given number is prime number or not 

import sys 
number = int(input("Enter number")) 
divisor = 2
while divisor<number: # 2 3 4 5 6
    reminder = number % divisor
    if reminder == 0:
        print("it is not prime number")
        sys.exit(1) #program stop 
    else:
        divisor = divisor + 1 #3

print("it is prime number")