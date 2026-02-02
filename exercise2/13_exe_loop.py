
# write a program to convert all negative values into positive values in the same list 

list=[12, -45, 7, -3, 89, -22, 0, 34, -9, 56]

print("Old list is : ",list)

for no in list:
    if no<0:
        list[list.index(no)] = no *-1
        

print("New list is :",list)

