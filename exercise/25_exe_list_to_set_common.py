# Given two lists, convert them into sets and find common elements
list1 = [1,2,3,44,6,7]
list2 = [12,26,3,44,68,71]

set1 = set(list1)
set2 = set(list2)

print(f"Common elements are : {set1.intersection(set2)}")