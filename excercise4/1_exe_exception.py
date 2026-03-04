# example of exception handling with list 
# write a program to calculate total and average score by team members in cricket match

scoreboard = ['tushar', 12, 57, 4, 96, 28, 71, 39, 65, 2, 90]
count=0
total=0

try:
     for run in scoreboard:
          total=total+run
          count=count+1
except TypeError:
     print("invalid type so value is skipped")

try:
     avg=total/count
except ZeroDivisionError:
      print("all values are invalid, so no total & average is generated")
else:
     print("total is:",total,"average is:",avg)