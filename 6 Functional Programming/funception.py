#function that takes the outputs of a function and sets it to the power of itself
def exp(func, arg):
    return (func(arg)) ** (func(arg))
#takes a number and subtracts 5
def minfive(x):
    return x - 5
#prints 50**50
print(exp(minfive,55))