#Only immutable objects can be keys. Lists and dictionaries are a big nono. Key:value
height = {"Jake":178, "Ryder":154, "Thomas":201, "Harry":182}
print(height["Ryder"])
#value of Ryder's height is reassigned
height["Ryder"] = 200
print(height["Ryder"])
#can find if keys are in dictionary. NOT VALUES
print("Ryder" in height)
print(201 in height)
print("Joseph" not in height)
#get is like indexing but you can specify what is printed if the key isn't found
print(height.get("Jake"))
print(height.get("Homer"))
print(height.get("Sally", "big yikes"))