"""write a program to accept month number from user and display how many days month has. (use logical operator or)
    input : 1 output : this month has 31 days 
    input : 4 output : this month has 30 days """
n = int(input("Enter Month : ")) 
if n==2:
    print("This month has 28 or 29 days")
elif n==4 or n==6 or n==9 or n==11 :
    print("This month has 30 days")
elif n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12:
    print("This month has 31 days")
else:
    print("Invalid Month")
