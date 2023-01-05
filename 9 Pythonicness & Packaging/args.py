#when *args is used, an arbitrary number of arguments can be given to a function
#*args is a tuple
#useful if you don't want to create an iterable before running the function
def funcboy(realarg, *args):
    print(realarg)
    print(args)
funcboy(1,2,3,4,5)