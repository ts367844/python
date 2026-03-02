# example of exception handling with list 
# write a program to calculate total and average score by team members in cricket match 
total = 0
# scoreboard = [83, 12, 57, 4, 96, 28, 71, 39, 65, 2, 90]
# scoreboard = [None,12, 'Rinku',57, 4, 96, 28, 71, 39, 65, 2, 90]
# scoreboard = ['Rinku','Rohit','Kohli']
scoreboard = None 
count = 0
try:
    for runs in scoreboard:
        total = total + runs 
        count = count + 1
except TypeError:        
    print('invalid type so value is skipped')
try:
    average = total / count
except ZeroDivisionError:
    print("all values are invalid, so no total & average is generated")
else:
    print("total runs ",total," Average",average)