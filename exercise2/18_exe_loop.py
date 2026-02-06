"""
  5 4 3 2 1
  5 4 3 2
  5 4 3
  5 4
  5
"""

for i in range(6,1,-1):
    count=5
    for j in range(1,i):
        print(count,end=" ")
        count-=1
    print()