#  write a program to decide which is cheaper approach to go from ahmedabad to delhi. by car or by train. consider person has his own petrol car  and he prefer to travel by 1st class train 
ahmdabad_to_delhi_km = 986
price_fuel = 95
average_of_car = 9
by_car = (ahmdabad_to_delhi_km/average_of_car) * 95
by_train = 3945
if by_car>by_train:
    print("Train is cheaper")
else:
    print("Car is cheaper")