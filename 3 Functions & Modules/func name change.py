#imports math functions for use of math.sqrt
import math
#defining our distance formula function
def distance(x,y,a,b):
#important that you use math. when accessing functions from math
    i = math.sqrt((a-x)**2 + (b-y)**2)
#i is used to store the answer for later
    return i
#distance is renamed to dist so it is shorter, important that dist comes first as that is what we are assigning the distance function
dist = distance
#storing the answer for dist() in ans
ans = dist(1,2,3,4)
print(ans)