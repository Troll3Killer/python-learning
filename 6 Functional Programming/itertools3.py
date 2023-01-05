from itertools import product, permutations
alpha = ["A", "B", "C"]
omega = [1, 2, 3]
#makes a list with every combination of each value
print(list(product(alpha, omega)))
#makes a list with all possible orders of values
print(list(permutations(alpha)))