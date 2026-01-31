# write a program to count odd and even number in numeric list 

odd=0
even=0

list=[1,2,3,4,5,6,7,8,9,10,11]


for no in list:
    if no%2==0:
        even+=1
    elif no%2!=0:
        odd+=1

print(f"Total Even Number are {even}")
print(f"Total Odd Number are {odd}")