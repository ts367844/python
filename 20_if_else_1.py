# write a program to find out which is cheaper product to purchase from 2 product's weight and price. 

p1 = float(input("Enter price of product 1 : "))
w1=float(input("Enter weight of product 1 :"))

p2 = float(input("Enter price of product 2 : "))
w2=float(input("Enter weight of product 2 :"))

price_per_gram1 = p1/w1
price_per_gram2 = p2/w2

if price_per_gram1>price_per_gram2:
    print("Second product is cheaper : ",price_per_gram1-price_per_gram2)
else:
    print("first is cheaper  : ",price_per_gram2-price_per_gram1)