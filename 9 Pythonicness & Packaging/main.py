#most code is either a module or a script
#you can make code not run if it is being used as a module
def funky():
    print("This function is for a module")
#__name__ is a special variable that is changed depending on if it is a script or module
#if it is a script then it is changed to __main__,
#if not it is changed to the name of the file
if __name__ == "__main__":
    print("This is a script")