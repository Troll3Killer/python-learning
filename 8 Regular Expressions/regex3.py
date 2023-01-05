import re
#raw string
search = r" is "
merch = re.search(search, "The only thing keeping this box together is scraps of cardboard and duct tape")
if merch:
    print("MATCH!!!")
    #prints string that matches
    print(merch.group())
    #prints start position of string
    print(merch.start())
    #prints end position of string
    print(merch.end())
    #prints tuple with start and end position
    print(merch.span())
else:
    print("no match, very sad")