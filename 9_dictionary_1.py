# dictionary 1
user_data = {'name':'tushar','age':20,'weight':73.00,'gender':True,'isMarried':False}
print(user_data)
print(user_data['name'])
# update a value
user_data['name'] = 'tushar makwana'
# add a new values
user_data['place'] ='bhavnagar'
user_data['pincode'] = 364001
print(user_data)
# delete a values
del user_data['weight']
print(user_data)