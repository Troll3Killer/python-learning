#puts text file into list in variable x
x = open("C:\\Users\\tlee\\Documents\\Programming\\Python Serious Time\\4 Exceptions & Files\\testfile.txt", "r")
#readlines takes entire file into memory so it is better to use for loop. Achieves basically the same thing
print(x.readlines())
#file closed
x.close