# for loop wicth string
# count vowels
n= input("Enter your name:")
vowels = ['a','e','i','o','u']
count = 0
for letter in n:
    if str.lower(letter) in vowels:
        count+=1
print(count)