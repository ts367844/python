"""
19)
* * * * *
 * * * *
  * * *
   * *
    *
    *
   * *
  * * *
 * * * *
* * * * *
"""

nsp=0
nst=5
for i in range(1,6):
    
    
    for j in range(1,nsp+1):
        print("",end=" ")
    
    for j in range(1,nst+1):
        print("* ",end="")
    
    print("")
    nst-=1
    nsp+=1

nst=1
nsp=4
for i in range(1,6):
    for j in range(1,nsp+1):
        print("",end=" ")
    
    for j in range(1,nst+1):
        print("* ",end="")
    
    print("")
    nst+=1
    nsp-=1