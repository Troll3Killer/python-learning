#while loop to make program run more than once
while True:
#operator is put into op variable
    print("Enter your operator")
    op = input("")
#first number put in var num1 and turned into integer, non-integers will break program
    print("Enter your first number")
    num1 = int(input(""))
#second number put in var num2 and turned into integer
    print("Enter your second number")
    num2 = int(input(""))
#op var compared with operators to see what matches so it can perform action on num1 and num2
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "%":
        print(num1 % num2)
    elif op == "//":
        print(num1 //num2)
    elif op == "**":
        print(num1 ** num2)
#if it doesn't match an operator the program will end
    else:
        print("Wrong Operator Entered, Ending Program")
        break