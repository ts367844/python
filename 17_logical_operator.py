# logical operator in python
n1 = int(input("Enter number 1:"))
n2 = int(input("Enter number 2:"))
n3 = int(input("Enter number 3:"))

res = n1 < n2 and n2 < n3
print(f"{res} = {n1}<{n2} and {n2}<{n3}")

res = n1 < n2 and n2 > n3
print(f"{res} = {n1}<{n2} and {n2}>{n3}")

res = n1 < n2 or n2 > n3
print(f"{res} = {n1}<{n2} or {n2}>{n3}")

res = n1 > n2 or n2 > n3
print(f"{res} = {n1}>{n2} or {n2}>{n3}")

res = not(n1 < n2 and n2 < n3)
print(f"{res} = not {n1}<{n2} and {n2}<{n3}")