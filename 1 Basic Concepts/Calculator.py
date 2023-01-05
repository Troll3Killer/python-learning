x = input("Enter your operator:")
if x == "+":
    print(float(input("First Number:")) + float(input("Second Number:")))
elif x == "-":
	print(float(input("First Number:")) - float(input("Second Number:")))
elif x == "*":
	print(float(input("First Number:")) * float(input("Second Number:")))
elif x == "/":
	print(float(input("First Number:")) / float(input("Second Number:")))
elif x == "%":
	print(float(input("First Number:")) % float(input("Second Number:")))
elif x == "//":
	print(float(input("First Number:")) // float(input("Second Number:")))
elif x == "**":
	print(float(input("First Number:")) ** float(input("Second Number:")))
elif x == "cheese":
	print("CHEESE " + str(input("Cheesify word:")))
else:
	print("ERROR")
print("Program Terminated")