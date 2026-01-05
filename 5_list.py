# list 1
random_values = ["apple",42,"python",3.14,True,"banana",7,"AI",99.9,"code"]
print(random_values)
# add item
random_values.insert(0,44)
print(random_values)
# add item to last index
random_values.append(88)
print(random_values)
# update item
random_values[1]="India"
print(random_values)
# delete item
del random_values[2]
print(random_values)
# delete by value
random_values.remove('python')
print(random_values)
# delete item using index
random_values.pop(2)
print(random_values)
# delete whole list
del random_values