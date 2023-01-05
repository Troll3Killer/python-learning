def yeet(x):
    return x >= 5
number = [1,3,4,5,7,9,11]
sift = list(filter(yeet,number))
print(sift)