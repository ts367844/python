# Write a program to calculate discount amount using price and discount rate.

i1 = int(input("Enter Amount of an Item 1 : "))
i2 = int(input("Enter Amount of an Item 2 : "))
i3 = int(input("Enter Amount of an Item 3 : "))
i4 = int(input("Enter Amount of an Item 4 : "))
rate = int(input("Enter Discount Rate(%) : "))

print(f"Discount Amount is : {(i1+i2+i3+i4)*rate/100}")