#write a program to convert given grams into kg and remaining grams
# input : 2500 grams
# output : 2 kg and 500 grams 

n1 = int(input("Enter grams :"))

kg = n1 // 1000
gram = n1 % 1000
print(kg," kg  and ",gram," grams")