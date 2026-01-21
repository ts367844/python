# write a program to accept length and width of two different farm from user. and find out & display which farm is bigger 
length1 = int(input("Enter Length 1 : "))
width1 = int(input("Enter Width 1 : "))
length2 = int(input("Enter length 2 : "))
width2 = int(input("Enter width 2 : "))
area1 = length1 * width1
area2 = length2 * width2

if area1>area2:
    print("First farm is bigger")
else:
    print("Second farm is bigger")