"""

  1
  0 1
  0 1 0
  1 0 1 0
  1 0 1 0 1

"""

count=1

for i in range(1,6):
    for j in range(1,i+1):
        print(count,end=" ")
        if count==1:
            count=0
        else:
            count=1
    print()