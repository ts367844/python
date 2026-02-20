# this is module
#create function to convert meter into inches
def meterToInch(meter):
    #here inch variable is local variable (declared inside function is called local variable, available to access only inside function where it is created)
    inch = meter * 39.37
    return inch 
#create function to convert foot into inches
def footToInch(foot):
    #here inch variable is local variable (declared inside function is called local variable, available to access only inside function where it is created)
    inch = foot * 12
    return inch 
#create function to convert cm into inches
def cmToInch(cm):
    #here inch variable is local variable (declared inside function is called local variable, available to access only inside function where it is created)
    inch = cm / 2.54
    return inch 
    