#explicitly changes values
class Dog:
    def __init__(self):
        self._age = 0
    def get_age(self):
        print("getting")
        return self._age
    def set_age(self, a):
        print("setting")
        self._age = a
    def del_age(self):
        print("deleting")
        del self._age
    age = property(get_age, set_age, del_age)
Lucy = Dog()
Lucy.age = 8
print(Lucy.age)
del Lucy.age