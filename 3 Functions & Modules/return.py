#function for adding !!! to any string
def excl(asdf):
    asdf = input("What are you excited about?\n")
    asdf += "!!!"
#return lets you store function output for later
    return asdf
#This shows that any code after return will not be used
    print("If this is printed big yikes!")
#any argument in excl() will work as it is reassigned when the function is called
z = excl(0)
#printed twice to show that z can be used more than once now that the function output is stored as a variable
print(z)
print(z)