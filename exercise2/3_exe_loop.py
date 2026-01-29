# 1    -8   27  -64  .....    1000
n = 1
square = 0
while n<11:
    square = n * n * n
    if square%2==0:
        square = 0 - square
    print(square,end=' ')
    n+=1 