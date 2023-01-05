#sets are like lists, except they are unordered so cannot be indexed
#they cannot contain duplicate values
#they are faster to check than a list
#use add rather than append to add to a set
#remove to remove an element from the set and pop to remove an arbitrary element (first element??)
stupid = {1,1,1,2,1,1,3,3,1,1,4,6,4,1}
print(stupid)
stupid.add(0)
print(stupid)
stupid.remove(1)
print(stupid)
stupid.pop()
print(stupid)