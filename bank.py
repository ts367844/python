balance = 1000
def deposit(amount):
    global balance 
    if amount<0:
        print("amount can not be less then 0")
    else:
        balance = balance + amount

def withdraw(amount):
    global balance
    if amount>0:
        print("Amount can not be greater then 0")
    else:
        balance = balance + amount 