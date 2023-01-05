word = input("Are you okay?\n")
if word[0] == "Y" or word[0] == "y":
    print("That's good")
elif word[0] == "N" or word[0] == "n":
    print("You should get that checked out")
else:
    print("Huh?")