""" write a program to accept 2 number from user. and accept choice for operations.
operations will be addition, subtraction, multiplication, division
do operation and display result as per user choice about operation using if elif else statements"""
n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))
ch = input("Enter Choice(+,-,*,/) :")
if ch=='+':
    print(f"Addition is :{n1+n2}")
elif ch=='-':
    print(f"Subtraction is :{n1-n2}")
elif ch=='*':
    print(f"Multiplication is :{n1*n2}")
elif ch=='/':
    print(f"Division is :{n1/n2}")
else:
    print("Invalid Choice")