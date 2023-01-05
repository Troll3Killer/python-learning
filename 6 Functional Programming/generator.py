#generators are iterables like lists or tuples, but are created using functions and yield.
#generators don't store the entire output in memory at once like lists do.
def big_to_small():
    i = 1000
    while i>=0:
        #yield continues the function instead of stopping like return does
        yield i**3
        i -= 1
for i in big_to_small():
    print(i)