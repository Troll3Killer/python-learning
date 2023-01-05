class Dog:
    def __init__(self):
        self._age = 0
    #@property replaces property(), so the method under it is the getter, then the next two define the setter and deleter
    @property
    def age(self):
        print("getting")
        return self._age
    @age.setter
    def age(self, a):
        print("setting")
        self._age = a
    @age.deleter
    def age(self):
        print("deleting")
        del self._age
Lucy = Dog()
Lucy.age = 8
print(Lucy.age)
del Lucy.age