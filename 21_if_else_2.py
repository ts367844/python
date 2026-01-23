'''
write a program to convert 24 hours time into 12 hours format time and display it with AM PM message. 
input : 15 hours 
output  3 PM 

input : 11 hours 
output  11 AM 

'''
hours = int(input("Enter hour :"))
if hours<0:
    hours = 0 - hours 

if hours>12:
    hours = hours - 12 
    ampm = " PM"
else:
    ampm = " AM"

print("Time is : ",hours,ampm)