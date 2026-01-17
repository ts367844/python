#write a program to findout whether number exist in list or not using in operator

numbers = [11, 44, 7, 89, 22, 55, 99, 33, 66, 14]

chk =int(input("Enter number in list  :"))
print("Number is in ",chk in numbers)

chk =int(input("Enter number in not  list  :"))
print("Number is in ",chk not in numbers)