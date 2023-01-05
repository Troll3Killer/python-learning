#classes define objects using methods(functions)
class Human:
    #__init__ is a necessary method that uses the objects name as the function name
    #the first argument is necessary but does not need to be self, just any word that makes sense
    #ex: __init__(myobject)
    #myobject.hair = hair
    def __init__(self,hair,eyes,age):
        #self refers to the object. For the object Tyler self.hair == Tyler.hair
        self.hair = hair
        self.eyes = eyes
        self.age = age
Tyler = Human("brown", "brown", 19)
John = Human("black", None, None)
print(Tyler.eyes)
print(John.age)