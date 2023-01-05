#this function calls itself, thus making it recursive. The else ends the function once the if is not satisfied
def recursion(x):
    if x>0:
        return x + recursion(x-1)
    else:
        return x
print(recursion(int(input("What would you like to recursively add?\n"))))