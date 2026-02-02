#write a program to count vowels, consonants, digits, words, and symbol in given list


string=input("Enter String : ")
digit=['1','2','3','4','5','6','7','8','9','0']
vowel=['a','e','i','o','u']
consonants =['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
d=0
v=0
c=0
s=0

for char in string:
    if char in digit:
        d+=1
    elif char.lower() in vowel:
        v+=1
    elif char.lower() in consonants:
        c+=1
    else:
        s+=1


print("Total words are : ",len(string.split()))
print("Digit are : ",d)
print("Vowels are : ",v)
print("Consonants are : ",c)
print("Special symbols are : ",s)