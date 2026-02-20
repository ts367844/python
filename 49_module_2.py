import bank 
amount = int(input("Enter deposit amount"))
print("balance before deposit ",bank.balance)
bank.deposit(amount)
print("balance after deposit ",bank.balance)
amount = int(input("Enter withdrawal amount"))
bank.withdraw(amount)
print("balance after withdrawal ",bank.balance)