#arbhitary  function
#*value means tuple
def getResult(*values):
   
    print(f"count = {len(values)} total = {sum(values)} average = {sum(values)/len(values)}")

getResult(10,20,45,87)