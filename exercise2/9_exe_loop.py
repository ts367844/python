# write a program to generate and display sum of all the float values in tuple and also calculate average

tp= (1.0, 2.5, 3.14, 4.0, 5.5, 6.7, 7.0, 8.8, 9.9, 10.0)

sum=0

for no in tp:
    sum+=no

print(f"Sum is : ",sum)
print("Average is :",sum/len(list(tp)))