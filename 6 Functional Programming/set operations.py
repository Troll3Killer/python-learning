bah = {11,22,33,44,55,66,77}
boo = {55,66,77,88,99,110}
#union combines sets to create a new set with values from both sets
print(bah | boo)
#intersection gets items from both sets
print(bah & boo)
#difference gets items from first set not in second set
print(bah - boo)
print(boo - bah)
#symmetric difference gets items from either set not in both sets
print(boo ^ bah)