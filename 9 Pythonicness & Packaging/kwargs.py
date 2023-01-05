#**kwargs let's you make the argument names when you are using the function
#**kwargs are a dictionary
def funkyboy(x, y=10, *args, **kwargs):
    print(kwargs)
#1 and 2 are x and y, 3-7 are *args, 8 and 9 are **kwargs
funkyboy(1,2,3,4,5,6,7,a=8,b=9)