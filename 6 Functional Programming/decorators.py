#decorators modify functions using other functions
#defines variable going to printer()
x = input("what?\n")
#decorator function
def dec(funcboy):
    #nested function so I can return the function
    def wrapper():
        print("==========")
        funcboy()
        print("==========")
    return wrapper
def printer():
    print(x)
#defining a function that uses printer function in the decorator function
finished = dec(printer)
#runs finished()
finished()