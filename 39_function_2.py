import shutil as s
width=s.get_terminal_size().columns
#Function without argument and no return value
def printLine():
    print('-'*width)

#Function with argument and no return value
def printMessage(msg):
    print(msg.center(width))

#Function with no argument but return value
def getPi():
    
    return 22/7

printLine()
printMessage('Hello World')
printLine()
print(f"Pi ={getPi()}")