#write a program to convert given minutes into hours and remaining minutes
#input : 150 minutes 
#output : 2 hours and 30 minutes 

min = int(input("Enter minutes ")) #Getting min from user

hr =min//60  #Getting hour
min=min %60  #Getting min
print(f"{hr} hours and {min} minutes") #Displaying minutes