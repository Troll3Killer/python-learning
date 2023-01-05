#shows that raise will stop code after it unless it is finally
try:
    print(1)
    #raise does not need to be in a try. String can be added in () to give detail to error
    raise ZeroDivisionError("I am a cheeky boi")
    print(2)
finally:
    print("end")