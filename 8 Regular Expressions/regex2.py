import re
#raw string
search = r" is "
#matches if search is at start of string
if re.match(search, "The only thing keeping this box together is scraps of cardboard and duct tape"):
    print("MATCH!!!")
else:
    print("no match, very sad")
#matches if search is anywhere in string
if re.search(search, "The only thing keeping this box together is scraps of cardboard and duct tape"):
    print("MATCH!!!")
else:
    print("no match, very sad")
#makes a list of all matches
print(re.findall(search, "The only thing keeping this box together is scraps of cardboard and duct tape"))