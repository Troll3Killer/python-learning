import re
#groups with a ?: in them are not shown when doing .group() or .groups()
#groups can be named
search = r"(?P<yeet>The) (?:only) (thing)"

string = re.search(search, "The only thing holding this box together is scraps of cardboard and duct tape.")
if string:
    print(string.group("yeet"))
    print(string.groups())