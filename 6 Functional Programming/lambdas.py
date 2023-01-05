#lambdas let you make functions that can fit on a single line, ususally within another function
#normal function
def ahh(g):
    return 6*g + 808
print(ahh(6))
#lambda
print((lambda h: 6*h + 808)(6))