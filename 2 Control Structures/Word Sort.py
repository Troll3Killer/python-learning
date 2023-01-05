first = input("Type the first word:")
second = input("Type the second word:")
if first < second:
    print("The first word comes before the second")
elif second < first:
    print("The second word comes before the second")
else:
    print("An Error occured. Sorry!")