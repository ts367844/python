#multiple return values function

def getResult(*values):
   
    return len(values),sum(values),sum(values)/len(values)

result=getResult(10,20,45,87,80)
print(result)