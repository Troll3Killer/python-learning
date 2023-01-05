#when you list slice it gives you a new list with the old list values between your parameters
hoo = ["dumb", "moredumb", 1, 2, 3, 4, "bigdumb", "I don't want this"]
#like range keeps value of first number but not second number, so it's 2,3,4,5
print(hoo[2:6])
#tuples can be sliced
ha = ("hmmm", "harhar", "haha", "yikeroos")
#goes from the beginning to 1
print(ha[:2])
#goes from 1 to the end
print(ha[1:])
#steps
print(hoo[::2])
#for first and second value, negative numbers count from end of list
print(hoo[1:-1])
#for third value -1 will reverse the list
print(hoo[::-1])