# dictionary 3
user_data = {'name':'tushar','age':20,'weight':73.00,'gender':True,'isMarried':False}
print(user_data)
print(user_data.get('age'))
print(user_data.get('city')) # error
# copy a dictionary
user_data2 = user_data.copy()
user_data2.clear()#remove a all values
print(user_data2,user_data)
# display only keys
print(user_data.keys())
print(user_data.values())
print(user_data.items())
book = ['name','author','pages','price','isbnno']
python_book = dict.fromkeys(book)
print(python_book)
# update a values
python_book['name'] = "Python" 
python_book['author'] = "the easylearn" 
# add/create a values
python_book['publisher'] = "ABC" 
print("now python book has",python_book)
# remove a values
python_book.pop('price')
python_book.pop('country',False)
python_book.popitem() #remove last key value pair
print(python_book)