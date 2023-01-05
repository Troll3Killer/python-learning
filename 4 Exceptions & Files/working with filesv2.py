#easier way to open and close files without try and finally, with will automatically close the file at the end of the with block
with open("C:\\Users\\tlee\\Documents\\Programming\\Python Serious Time\\4 Exceptions & Files\\testfile.txt") as f:
    print(f.read())