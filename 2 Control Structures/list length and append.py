list = []
while True:
    x = input("What do you want in the list? Type end to continue\n")
    if x == "end":
        break
    list.append(x)
print(str(len(list)) + "\nThis is the length of the list")
print(list)