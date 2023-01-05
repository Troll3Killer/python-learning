#try and finally method of working with files
try:
    x = open("C:\\Users\\tlee\\Documents\\Programming\\Python Serious Time\\4 Exceptions & Files\\testfile.txt")
    print(x.read())
#finally ensures the file is closed
finally:
    x.close()