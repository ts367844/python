# write a program to convert 24 hours time into 12 hours format time and display it with AM PM message. 
#         input : 15 hours 
#         output  3 PM 

#         input : 11 hours 
#         output  11 AM 

#         input : 25 hours 
#         output  invalid input 
n = int(input("Enter hour : "))
if n>12:
    print(f"{n-12} PM")
if n<=12:
    print(f"{n} AM")
if n>24 or n<0:
    print("Invalid input")