import re
#r'' means it is a raw string
search = r"tape"
#re.match matches regex to a string, always starts from beginning of string
if re.match(search, "The only thing keeping this box together is scraps of cardboard and duct tape"):
    print("MATCH!!!")
else:
    print("no match, very sad")