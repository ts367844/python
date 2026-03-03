import converter as c 
#here c is alias for converter, instead of writing converter, we can use c 
#take input meter, foot, cm 
meter = float(input("Enter value in meters: "))
foot = float(input("Enter value in feet: "))
cm = float(input("Enter value in centimeters: "))

inch = c.meterToInch(meter) 
print(f"{inch} of {meter} meter")

inch = c.footToInch(foot)
print(f"{inch} of {foot} foot")

inch = c.cmToInch(cm)
print(f"{inch} of {cm} cm ")
