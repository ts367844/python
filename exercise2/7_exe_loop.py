#write a program to figure out whether given number  is armstrong number or not
no=int(input("Enter number : "))
no2=no
count=len(str(no))
sum=0
while no2>0:
    ld=no2%10
    sum+=pow(ld,count)
    no2//=10
if sum==no:
    print("Armstrong number ")
else:
    print("Not Armstrong number ")