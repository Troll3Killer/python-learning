#map lets you use a function on an iterable like a list
def double(x):
    return 2*x
numb = [1,2,3,4,5,6,7,8,9,10]
boom = list(map(double,numb))
print(boom)