#  write a program to find out whether given year is millennium year or not. using if else decision making statements
n = int(input("Enter Year : "))
if n % 1000 == 0:
    print("Year is millennium")
else:
    print("Year is not  millennium")