# Write a program to calculate total amount after simple interest

p = int(input("Enter Rate : "))
r = int(input("Enter Principal Amount : "))
n = int(input("Enter Year : "))

si = ((p*r*n)/100)
print(f"Total Amount is :{si+p}")