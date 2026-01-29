#write a program to convert given 3 digit amount into words
# input : 175 output : one seven five 

#Getting amount
no = input("Enter 3 digit amount: ")
#Converting into int
no = int(no)
a =no
# get a first element
f = a//100
a = a //10 
# get a middle element  
m = a %10 
# get a last element
l = no % 10 
#List 
words=['zero','one','two','three','four','five','six','seven','eight','nine']
print(words[f]+" "+words[m]+" "+words[l])