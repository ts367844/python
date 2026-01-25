# write a program to print following series 
# 1     -4      9     -16     25      -36     1000
# 1     2       3       4       5       6    
n = 1
square = 0
while n<=31: 
    square = n * n
    reminder = square % 2
    if reminder==0:
        square = 0 - square
    print(square,end=' ')
    n += 1