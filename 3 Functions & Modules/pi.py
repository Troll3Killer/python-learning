#when something is specifically pulled from a module you can use it without have math. in front of it. Use , to add more than one. Use * to add all, but not recommended.
from math import pi
#used to repeat program
while True:
    option = input("Would you like to find the circumference or the radius?\n")
    #calculates cirumference
    if option == "circumference":
        rad = float(input("What is the radius?\n"))
        print("The answer is " + str(rad * 2 * pi))
        continue
    #calculates radius
    elif option == "radius":
        cir = float(input("What is the circumference?\n"))
        print("The answer is " + str(cir/(2*pi)))
        continue
    #ends program happy
    elif option == "quit":
        print("Have a nice day!")
        print('''
              _.--""`-..
            ,'          `.
          ,'          __  `.
         /|          " __   \\
        , |           / |.   .
        |,'          !_.'|   |
      ,'             '   |   |
     /              |`--'|   |
    |                `---'   |
     .   ,                   |                       ,".
      ._     '           _'  |                    , ' \ `
  `.. `.`-...___,...---""    |       __,.        ,`"   L,|
  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \\
-:..     `. `-..--_.,.<       `"      / `.        `-/ |   .
  `,         """"'     `.              ,'         |   |  ',,
    `.      '            '            /          '    |'. |/
      `.   |              \       _,-'           |       ''
        `._'               \   '"\                .      |
           |                '     \                `._  ,'
           |                 '     \                 .'|
           |                 .      \                | |
           |                 |       L              ,' |
           `                 |       |             /   '
            \                |       |           ,'   /
          ,' \               |  _.._ ,-..___,..-'    ,'
         /     .             .      `!             ,j'
        /       `.          /        .           .'/
       .          `.       /         |        _.'.'
        `.          7`'---'          |------"'_.'
       _,.`,_     _'                ,''-----"'
   _,-_    '       `.     .'      ,\\
   -" /`.         _,'     | _  _  _.|
    ""--'---"""""'        `' '! |! /
                            `" " -' mh
        ''')
        break
    #ends program neutral
    else:
        print("invalid input. Ending program")
        break