"""
Write a program that takes a 5 subject marks from user. calculate total and average  and prints the grade using the following conditions:

| Percentage | Grade |
| ---------- | ----- |
| 90-100     | A+    |
| 80-89      | A     |
| 70-79      | B     |
| 60-69      | C     |
| 50-59      | D     |
| below 50   | Need to improve  |
----------------------------------------
"""
s1 = int(input("Enter mark of Subject 1 : "))
s2 = int(input("Enter mark of Subject 2 : "))
s3 = int(input("Enter mark of Subject 3 : "))
s4 = int(input("Enter mark of Subject 4 : "))
s5 = int(input("Enter mark of Subject 5 : "))
tot = s1+s2+s3+s4+s5
per = tot/5
if per>=90:
    print(f"Percentage is {per} Grade is A+")
elif per>=80:
    print(f"Percentage is {per} Grade is A")
elif per>=70:
    print(f"Percentage is {per} Grade is B")
elif per>=60:
    print(f"Percentage is {per} Grade is C")
elif per>=50:
    print(f"Percentage is {per} Grade is D")
else:
    print(f"Need to improve percentage is :{per}")