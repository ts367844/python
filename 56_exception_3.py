#write a program to accept transfer amount from user & transfer amount. if amount>balance or greater then daily transfer limit raise custom exception 
class TransferLimitException(Exception):
    pass 
balance = 987525
daily_limit = 100000
try:
    amount = int(input("enter transaction amount"))
    if amount>balance:
        raise TransferLimitException("insufficient balance in your account")
    elif amount>daily_limit:
        raise TransferLimitException("transfer daily limit exceeded ")
    else:
        print("money transfer successful")
        balance = balance - amount
        print("remaining balance in your account ",balance)
except TransferLimitException as error:
    print(error)
finally:
    print("thank for banking with us")