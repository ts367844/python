# write a program to findout name of crickerter in string which has 20 player name using in operator.

cricketers = "virat kohli, rohit sharma, ms dhoni, sachin tendulkar, rahul dravid, sourav ganguly, yuvraj singh, hardik pandya, jasprit bumrah, ravindra jadeja, shikhar dhawan, kl rahul, rishabh pant, suryakumar yadav, mohammed shami, ishant sharma, bhubaneswar kumar, harbhajan singh, zaheer khan, anil kumble"


find=input("Enter name you want to search :")
print("The name you search is : ",find in cricketers)