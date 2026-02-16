# write a program to figure out binary of given decimal number 
def toBinary(number):
    if number>0:
        reminder = number % 2 
        number = number // 2 # 19 9 4 2 1 0
        toBinary(number) #recusion
        print(reminder,end=' ') # 1
number = int(input("Enter number"))
toBinary(number) # 1 0 0 1 1 