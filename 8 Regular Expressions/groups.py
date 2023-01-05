import re

search = r"This (is )+(very )+ridiculous says I!"

cheese = re.search(search, "This is is very very ridiculous says I!")
if cheese:
    #.group lets you see the string match in parentheses
    #.group() and .group(0) show the whole match
    print(cheese.group())
    print(cheese.group(0))
    #.group(#) show the value in parentheses from left to right
    print(cheese.group(1))
    print(cheese.group(2))
    #.groups() shows all of the groups
    print(cheese.groups())