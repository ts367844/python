#  write a program to accept day of week (between 1 to 7) and then display name of day. (use simple if decision making)
#             input 1 : monday 
#             input 2 : tuesday 
#             input 7 : sunday 
n = int(input("Enter day number : "))
if n==1:
    print("Monday")
if n==2:
    print("Tuesday")
if n==3:
    print("Wednesday")
if n==4:
    print("Thursday")
if n==5:
    print("Friday")
if n==6:
    print("Saturday")
if n==7:
    print("Sunday")
if n<1 or n>7:
    print("Invalid day")