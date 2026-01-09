# WAP to convert a two digit number into a words
# like input : 44 output : four four
no = input("enter 2 digit number :")
# convert string to integer
no = int(no)
# both digits in diffrence variable
f = no // 10
l = no % 10
# list for words
words = ['zero','one','two','three','four','five','six','seven','eight','nine']
print(words[f]," ",words[l])