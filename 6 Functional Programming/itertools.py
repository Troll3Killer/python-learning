from itertools import count,cycle,repeat
#count goes infinitely up from a value
for i in count(3):
    print(i)
    if i>=10:
        break
zapp = [10,9,8,7,6,5,4,3,2,1]
#cycle infinitely iterates through an iterable
for i in cycle(zapp):
    print(i)
    if i == 1:
        break
#repeats an object a certain number of times repeat(object, number of times)
for i in repeat(10,3):
    print(i)