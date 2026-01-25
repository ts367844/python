# write a program to find out which is cheaper product to purchase from 2 product's weight and price. 
# also display how much cheaper per gram 
p1 = float(input("Enter price of product 1 : "))
w1=float(input("Enter weight of product 1 :"))

p2 = float(input("Enter price of product 2 : "))
w2=float(input("Enter weight of product 2 :"))

if p1<=0 or p2<=0 or w1<=0 or w2<=0:
    print("Negative input is not allowed")
else:
    price_per_gram1 = p1/w1
    price_per_gram2 = p2/w2
    
    if price_per_gram1>price_per_gram2:
        print("Second product is cheaper : ",price_per_gram1-price_per_gram2)
    else:
        print("first is cheaper  : ",price_per_gram2-price_per_gram1)