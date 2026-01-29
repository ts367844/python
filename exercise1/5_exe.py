#write a program to display dinominations of currency for given amount
# input : 887 Rupees 
# output : 
# 500 x 1 = 500
# 200 x 1 = 200
# 100 x 1 = 100
# 50 x 1 =  50
# 20 x 1 =  20
# 10 x 1 =  10
# 5 x 1 =   05
# 2 x 1 =   02
# 1 x 1 =   01


n1 = int(input("Enter amount :"))

r500 = n1 // 500
n1 = n1 % 500

r200 = n1 // 200
n1 = n1 % 200

r100 = n1 // 100
n1 = n1 % 100

r50 = n1 // 50
n1 = n1 % 50

r20 = n1 // 20
n1 = n1 % 20

r10 = n1 // 10
n1 = n1 % 10

r5 = n1 // 5
n1 = n1 % 5

r2 = n1 // 2
n1 = n1 % 2

answer = f"""
    500 x 1 = {r500}
    200 x 1 = {r200}
    100 x 1 = {r100}
    50 x 1 = {r50}
    20 x 1 = {r20}
    10 x 1 = {r10}
    5 x 1 = {r5}
    2 x 1 = {r2}
    1 x 1 = {n1}
"""

print(answer)
