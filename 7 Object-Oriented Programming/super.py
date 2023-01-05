#methods with the same name in a subclass override the one in the superclass
class rectangle:
    def talk(self):
        print("I am a rectangle!")
class square(rectangle):
    def talk(self):
        print("I am a square and")
        #super() can be used to call the superclass version of a method in a subclass
        super().talk()
square().talk()