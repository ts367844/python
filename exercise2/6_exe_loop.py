# write a program to figure out whether given number  is perfect number or not

no = int(input("Enter number : "))
sum=1
divisor=2
half=(no//2)+1
while divisor <half:
    if no%divisor==0:
        sum+=divisor
    divisor+=1
if sum==no:
    print("Perfect number ")
else:
    print("Not Perfect number ")