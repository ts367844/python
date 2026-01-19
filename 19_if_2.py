# write a program to find out whether given shape is square or portrait or landscape using user given length and width 

length=float(input("Enter the length : "))
width=float(input("Enter the width : "))

if length== width:
    print(" its square ")

if length >width:
    print(" its landscape")

if length <width:
    print(" its portrait")