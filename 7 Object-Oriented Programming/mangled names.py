class Food:
    #methods starting with two underscores cannot be accessed outside the class with their normal name
    __egg = 12
    def printer(self):
        print(self.__egg)
s = Food()
s.printer()
#however they can be accessed by adding _className to the front of the method
print(s._Food__egg)
print(s.__egg)