# exercise of an dictionary
personal_details = {"first_name":"Tushar","last_name":"Makwana","age":20,"gender":"Male","date_of_birth":"2005-12-27","email":"tushar367844@gmail.com","phone":"9327542206","address":"gujarat, India","city":"Bhavnagar","state":"Gujarat","country":"India","pincode":"364001","nationality":"Indian","marital_status":False,"occupation":"Student","education":"BCA","blood_group":"B+","height_cm":170,"weight_kg":65,"language":"Hindi, English"}
print(personal_details)
print(personal_details['first_name']+personal_details['last_name'])
# add a pincode and five favourite destinations
personal_details['piincode'] = 364001
personal_details['favourite_destination'] = ['Rajsthan','Ladakh','Andaman','Anini','Amarnath']
# print a favourite destination
print(personal_details['favourite_destination'])