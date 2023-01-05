file = open("C:\\Users\\tlee\\Documents\\Programming\\Python Serious Time\\4 Exceptions & Files\\testfile.txt", "r")
#file.read(4) 4 specifies how many bytes to read
read = file.read(4)
print(read)
file.close()