#function takes argument x
def sum(x):
    #res variable created
    res = 0
    #creates a range from 0 to x, excluding x. For example, x=5 so 0,1,2,3,4
    for i in range(x):
        #for each number in this range, it adds it to res until it reaches the end of the range, effectively adding 0+1+2+3+4+...
        res += i
    #res is returned so the output can be used more than once if assigned to a variable outside the function
    return res
#printing sum(4) results in 6 because 0+1+2+3=6
print(sum(4))