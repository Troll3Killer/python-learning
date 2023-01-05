#try statement will try the following code and execute code in except if code in try fails.
try:
    num1 = float(input("num1\n"))
    num2 = float(input("num2\n"))
    print(num1/num2)
#if a number is divided by zero this code will run
except ZeroDivisionError:
    print("Can't divide by zero dumb-dumb")
#if someone puts anything other than a number this code will run
except (ValueError, TypeError):
    print("Error, you put something in wrong dumb-dumb")