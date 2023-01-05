import random
class Vague:
    #initial object creation
    def __init__(self, cheese):
        self.cheese = cheese
    #adds a value in a place within 2 spaces from the index chosen
    def __setitem__(self, index, value):
        yeet = self.cheese
        yeet.insert(index + random.randint(-2,2), value)
        return yeet
    #deletes a value from the list in the object
    def __delitem__(self, value):
        yeet = self.cheese
        yeet.remove(value)
        return yeet
v = Vague(["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Gamma"])
print(v.__setitem__(2,"let's goooooooo"))
print(v.__delitem__("Bravo"))
#good god was this hard to code