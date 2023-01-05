import math
#imports math library
a = float(input("A="))
b = float(input("B="))
c = float(input("C="))
#defines variables with user input
try:
    positive = (-b + math.sqrt(b**2 - 4*a*c))/2*a
    print(positive)
except:
    print("Negative Squareroot, go do it manually scrub")
try:
    negative = (-b - math.sqrt(b**2 - 4*a*c))/2*a
    print(negative)
except:
    print('Negative Squareroot, go do it manually scrub')