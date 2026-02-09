def getSquare(num):
    return num*num

def getCube(num):
    return getSquare(num)*num


no=int(input("Enter NUmber : "))
print(f"Square is :{getSquare(no)}")
print(f"Cube is :{getCube(no)}")