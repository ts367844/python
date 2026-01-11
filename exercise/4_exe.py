
#write a program to convert given grams into kg and remaining grams
#input : 2500 grams
#output : 2 kg and 500 grams 


g = int(input("Enter gram :")) #Getting gram from user

kg =g//1000  #Getting kf
g=g %1000  #Getting g
print(f"{kg} kg and {g} gram") #Displaying 