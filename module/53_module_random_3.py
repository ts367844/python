#generate random password  (letters in mixed case,digits,symbols)
import random as rd 
import string as st 
seeds = st.ascii_lowercase + st.ascii_uppercase + st.digits + st.punctuation
seeds = list(seeds)
rd.shuffle(seeds)
size = len(seeds) - 1
print(seeds)
count = 1
letter = []
while count<=32:
    letter.append(seeds[rd.randint(0,size)])
    count= count + 1
password = ''.join(letter)
print(password)