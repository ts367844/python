# write a program to find out whether given year is leap year or not
# https://www.wikihow.com/Calculate-Leap-Years
n = int(input("Enter Year :")) 
if n<1:
    print("Invalid Year")
else:
    reminder1 = n % 4
    reminder2 = n % 100
    reminder3 = n % 400
    if reminder1 == 0 and reminder2!=0:
        print("Leap Year = TRUE")
    else:
        if reminder2==0 and reminder3==0:
            print("Leap Year = TRUE")
        else:
            print("Leap Year = FALSE")