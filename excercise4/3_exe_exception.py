# example of exception handling with list 
# write a program to calculate total and average score by team members in cricket match 
total = 0
scoreboard = ["vivek", 12, 57, 4, -96, 28, 71, 39, 65, 2, 90]
count=0

for run in scoreboard:
    try:
        if run < 0:
            raise ValueError("number can't be nagetive so this value is skip")
        else:
            total=total+run
            count=count+1
    except TypeError:
        print("invalid type so value is not allow so this value is skipped")
    except ValueError as error:
        print(error)
try:
    avg=total/count
except ZeroDivisionError:
    print("number can't be zero")
else:
    print("total:",total,"average:",avg)


