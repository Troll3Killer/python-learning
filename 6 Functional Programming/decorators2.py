x = input("what?\n")
def dec(funcboy):
    def wrapper():
        print("==========")
        funcboy()
        print("==========")
    return wrapper
#@dec can be used rather than assigning the function in a function to another variable.
@dec
def printer():
    print(x)
printer()