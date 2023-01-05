#first function adds two arguments together
def add(x,y):
    return x+y
#second function squares the result of another function
def square(func,x,y):
    return func(x,y) * func(x,y)
print(square(add,3,5))