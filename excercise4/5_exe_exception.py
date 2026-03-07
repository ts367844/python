## write a program to find strike rate of batter using runs and balls 
#modify example 4, in case of 5 unsuccessful attempt program should stop

for a in range(1,6,+1):
    try:
        runs = int(input("Enter runs"))
        balls = int(input("Enter balls"))
        strike_rate = runs / balls * 100
        print(f"Strike rate = {strike_rate}")
        a=a+1
        break
    except ValueError as e:
        print("invalid input, runs and balls must be integers only ")
    except ZeroDivisionError as e:
        print("ball can not be zero")