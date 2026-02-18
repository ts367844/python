import math
#convert negative into postive using map and lambda 
numbers = [-45, 12, 78, -3, 0, 56, -89, 34, -21, 67, 5, -14, 92, -76, 18, -9, 41, -60, 23, -2]
positive_only = list(map(lambda num: math.fabs(num),numbers))
print(positive_only)