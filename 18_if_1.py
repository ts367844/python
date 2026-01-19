#Write a program to find profit or loss by purchase price or sell price

purchase_price=float(input("Enter purchase price :"))
sell_price=float(input("Enter selling price :"))

difference = sell_price - purchase_price 

if difference>0:
    print(f"Profit is of : {difference}")
if difference<0:
    print(f"Loss is of : {difference}")
if difference==0:
    print("No profit no Loss")