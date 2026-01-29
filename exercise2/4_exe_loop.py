#   0    1   1   2   3   5   8   13  .... 100
a=0
b=1
c=0
print(c,end=' ')
while c<89:
    c=a+b
    print(c,end=' ')
    b=a
    a=c