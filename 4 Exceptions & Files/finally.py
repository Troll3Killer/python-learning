try:
    print("yes")
    #this will trigger the except because there is no yikes variable
    print(yikes)
except:
    print("no")
#this will print no matter what 
finally:
    print("I will be here no matter what happens :D")