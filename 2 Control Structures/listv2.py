word = input("Are you okay?\n")
word = word.lower()
yeslist = ["yes","yeah","yep","yup","affirmative", "amen","fine","good","okay","true","yea","aye","certainly"]
nolist = ["no","nope","nah","nay","nix","never","not"]
if word in yeslist:
    print("That's good")
elif word in nolist:
    print("You should get that checked out")
else:
    print("Huh?")