back = list(input("What would you like to reverse?\n"))
back.reverse()
back = ''.join(back)
print(back)
######################
grocery = ["milk", "eggs", "bread", "chocolate"]
print(grocery)
grocery.remove("chocolate")
print(grocery)
######################
pascal = [1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1]
print(pascal.count(1))
######################
age = [17, 12,149, 12, 14, 2, 100, 23, 34, 65, 54, 34, 23, 15, 19]
print(max(age))
print(min(age))
print(age.index(12))