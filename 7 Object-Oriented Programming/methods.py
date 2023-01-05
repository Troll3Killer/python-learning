class Fish:
    #class attribute that applies to the entire class
    underwaterBreathing = True
    def __init__(self, name, color, length):
        self.name = name
        self.color = color
        self.length = length
    #method that can be used with object.talk
    #all methods need an argument to refer to themselves
    def talk(self):
        print("blub")
Goldie = Fish("Goldie", "gold", 5)
print(Goldie.name)
Goldie.talk()
print(Goldie.underwaterBreathing)