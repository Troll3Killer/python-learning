#lists can be created that follow specific rules
powerfour = [i**4 for i in range(10)]
print(powerfour)
#lists can be created with if's to enforce a condition
oddsqr = [i**2 for i in range(10) if i**2 % 2 != 0]
print(oddsqr)
#lists are stored completely in memory so you shouldn't make it too big, use generators for that stuff
try:
    yikes = [i for i in range(10**100)]
except MemoryError:
    print("you ran out of memory, download more RAM")