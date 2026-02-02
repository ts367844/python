#write a program to count digits in given string

string=input("Enter your string : ")
digits=0

for ch in string:
    if ch in ['1','2','3','4','5','6','7','8','9','0']:
        digits+=1


print(f"Digits are {digits}")