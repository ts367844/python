# example of exception handling with list 
# write a program to calculate total and average score by team members in cricket match 
total = 0
scoreboard = [83, 12, 57, 4, -96, 28, 71, 39, 65, 2, 90]
# scoreboard = [None,12, 'Rinku',57, 4, 96, 28, 71, 39, 65, 2, 90]
# scoreboard = ['Rinku','Rohit','Kohli']
# scoreboard = None 
count = 0
for runs in scoreboard:
    try:
        if runs<0:
            raise ValueError('negative score is not allowed, hence value is skipped')
        else: 
            total = total + runs 
            count = count + 1
    except TypeError:        
        print('invalid type so value is skipped')
    except ValueError as error:
        print(error)
try:
    average = total / count
except ZeroDivisionError:
    print("all values are invalid, so no total & average is generated")
else:
    print("total runs ",total," Average",average)