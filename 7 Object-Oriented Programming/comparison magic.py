class Planet:
    #defining object
    def __init__(self, name):
        self.name = name
    #defining greater than magic method
    def __gt__(self, other):
        #for loop that has a range equal to the length of the second value + 1
        for i in range(len(other.name)+1):
            #second object's name up to the number i happens to be plus > and first object name
            end = other.name[:i] + ">" + self.name
            #> and the rest of the second objects name
            end += ">" + other.name[i:]
            print(end)
mars = Planet("Mars")
venus = Planet("Venus")
mars > venus