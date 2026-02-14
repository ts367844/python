def getMerit(computer,drawing,english,history,maths,science):
    return maths + science + english
     

c = int(input("Enter marks for computer: "))
d = int(input("Enter marks for drawing: "))
e = int(input("Enter marks for english: "))
h = int(input("Enter marks for history: "))
m = int(input("Enter marks for maths: "))
s = int(input("Enter marks for science: "))


total = getMerit(maths=m,science=s,english=e,computer=c,drawing=d,history=h)
print(total)