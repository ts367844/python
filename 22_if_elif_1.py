#write a program to find out profit or loss amount from user given purchase and sell price of project
#input purchase & sell price    
purchase_p = float(input("Enter purchase price:"))
sale_p = float(input("Enter sale price:"))
difference = sale_p - purchase_p

if difference>0:
    print("Profit amount is:",difference)
elif difference<0:
    print("Loss amount is:",difference)
else:
    print("Neither loss nor profit")
