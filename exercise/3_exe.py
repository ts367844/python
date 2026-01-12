<<<<<<< HEAD
#write a program to convert given minutes into hours and remaining minutes
# input : 150 minutes 
# output : 2 hours and 30 minutes 

n1 = int(input("Enter Minutes :"))

hour = n1//60
minute = n1 %60
print(hour," hours  and ",minute," minutes")
=======
#write a program to convert given minutes into hours and remaining minutes
#input : 150 minutes 
#output : 2 hours and 30 minutes 

min = int(input("Enter minutes ")) #Getting min from user

hr =min//60  #Getting hour
min=min %60  #Getting min
print(f"{hr} hours and {min} minutes") #Displaying minutes
>>>>>>> 942a988cabf9b1fc2cebc12c8a5a3ef16dbd3a25
