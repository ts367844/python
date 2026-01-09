s1 = {5,44,67,94,56}
s2 = {51,46,88,94,56}
print(s1,s2)
#get unique values from both set (no repetation)
s3 = s1.union(s2)
print(s3)
# get a common value from a both set
s4 = s1.intersection(s2)
print(s4)
#get all values that is in one(s1) set but not in other set (s2)
s5 = s1.difference(s2)
print(s5)

# create a list that has a duplicate values
list1  = [5,44,88,67,94,56,44,88]
print(list1)
# remove a duplicate values from a list using a set(meance it can print only one time)
s6 = set(list1)
print(s6)