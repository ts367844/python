import random as rd 
#generate one random digit 
count = 1
digit = [] 
while count<=6:
    digit.append(str(rd.randint(0,9)))
    count=count + 1
digit = ''.join(digit) #convert list into string
print(digit)