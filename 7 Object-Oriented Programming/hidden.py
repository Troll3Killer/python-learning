#private methods do not really exist in Python, but if you don't want people to use a method,
#add an underscore in front of the method name
from random import randint
class Q:
    #insides value is turned into a list and assigned to the "private" method _hidden
    def __init__(self, insides):
        self._hidden = list(insides)
    #method that inserts a value randomly between the second and fifth value in the list
    def ruin(self, value):
        self._hidden.insert(randint(1, 4),value)
    #destroys the fifth value in the list
    def pop(self):
        return self._hidden.pop(4)
    #important magic method that makes printing the object return the list rather than nothing useful
    def __repr__(self):
        #.format changes the {} to be what's in the ()
        return "{}".format(self._hidden)
queue = Q([1,2,3,4,5,6,7,8])
print(queue)
queue.ruin(22)
print(queue)
queue.pop()
print(queue)
#this shows that _hidden can be called outside the class even though it is "private"
print(queue._hidden)