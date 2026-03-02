# write a program to find strike rate of batter using runs and balls 
while 1!=2:
    try:
        runs = int(input("Enter runs"))
        balls = int(input("Enter balls"))
        strike_rate = runs / balls * 100
        print(f"Strike rate = {strike_rate}")
        break
    except ValueError as e:
        print("invalid input, runs and balls must be integers only ")
    except ZeroDivisionError as e:
        print("ball can not be zero")