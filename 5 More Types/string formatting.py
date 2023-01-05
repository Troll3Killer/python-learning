numb = [10,9,8,7,6,5,4,3,2,1,0]
#{} refer to the position in .format, [] refer to position in list
text = "Numbers: {2} {0} {1}".format(numb[0], numb[1], numb[3])
print(text)
#values in .format do not need to reference a list
text2 = "Magic: {0}{1}{0}".format("abra","cad")
print(text2)
text3 = "Coordinates: {x}, {y}".format(x=4, y=6)
print(text3)