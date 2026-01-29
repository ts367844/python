# Write a program to calculate simple interest using principal, rate, and time

p = int(input("Enter Rate : "))
r = int(input("Enter Principal Amount : "))
n = int(input("Enter Year : "))

si = ((p*r*n)/100)
print(f"Simple Interset is :{si}")