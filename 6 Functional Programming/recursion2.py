#indirect recursion is when the first function calls the second which calls the first, causing a circular relationship
#I'll add the example given because it's really dumb compared to mine
#def is_even(x):
#  if x == 0:
#    return True
#  else:
#    return is_odd(x-1)
#def is_odd(x):
#  return not is_even(x)
#print(is_odd(17))
#print(is_even(23))
def even(x):
    if x % 2 == 0:
        return "Even"
    else:
        return odd(x)
def odd(x):
    if x % 2 != 0:
        return "Odd"
    else:
        return even(x)
print(even(13))
print(even(12))
print(odd(11))
print(odd(10))