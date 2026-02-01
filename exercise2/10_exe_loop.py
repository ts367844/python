#write a program to count words in given string 

string=input("Enter your string : ")
words=1

for ch in string:
    if ch==' ' :
        words+=1

print(f"Words are {words}")