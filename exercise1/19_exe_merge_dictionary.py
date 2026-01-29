# Merge two dictionaries into a single dictionary
student1 = {"a":75,"b":80,"c":66,"d":99,"e":59}
student2 = {"f":44,"g":78,"h":88}

# merge a dictionary
student1.update(student2)
print(f"Merged dictionary is : {student1}")