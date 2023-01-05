from itertools import takewhile,chain,accumulate
def goat(x):
    if x <= 2:
        return True
    else:
        return False
#accumulate creates a list that adds every number before it. example: [1,2,3,4,5] -> [1,3,6,10,15]
numb = list(accumulate(range(11)))
print(numb)
#chain combines iterables into one long one
hum = [1,2,3,4]
drum = {6,7,8,9}
tum = (20,21,22,23)
gum = list(chain(hum,drum,tum))
print(gum)
#takewhile takes items from an iterable as while something remains true
print(list(takewhile(goat,hum)))