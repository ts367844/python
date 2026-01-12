#write a program to convert given minutes into hours and remaining minutes
# input : 150 minutes 
# output : 2 hours and 30 minutes 

n1 = int(input("Enter Minutes :"))

hour = n1//60
minute = n1 %60
print(hour," hours  and ",minute," minutes")