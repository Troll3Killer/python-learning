#arguments can be given a default value for if a value is not given
#non-default arguments can not follow default arguments
def funcboy(x, y, animal = "Human"):
    print(x + y)
    print(animal)
funcboy(1,3)
funcboy(7,3,"Dog")