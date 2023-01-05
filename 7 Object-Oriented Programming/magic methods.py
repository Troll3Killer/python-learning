#magic methods are special methods with double underscores in the beginning and end of their names
#operator overloading can be used to define what operators do to an object
class A:
    #object is defined
    def __init__(self,color,name):
        self.color = color
        self.name = name
    #object add operation is defined
    def __add__(self, other):
        return self.color + other.color + self.name + other.name
first = A("blue","George")
second = A("orange","Popeye")
end = first + second
print(end)