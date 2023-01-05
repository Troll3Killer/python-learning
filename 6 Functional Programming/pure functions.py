#pure function
def pure(x,y):
    z = x**2+y**2
    return z
print(pure(2,3))

#impure function
list1 = [20,21]
def impure(garb):
    garb.append(112)
    return garb
print(impure(list1))