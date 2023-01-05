#opens file in write mode
x = open("C:\\Users\\tlee\\Documents\\Programming\\Python Serious Time\\4 Exceptions & Files\\testfile.txt", "w")
#overwrites file with string or creates new file if file doesn't exist
x.write("Haha, the stupid stuff you wrote is now gone")
#closes file
x.close
#opens file in read mode
x = open("C:\\Users\\tlee\\Documents\\Programming\\Python Serious Time\\4 Exceptions & Files\\testfile.txt", "r")
print(x.read())
x.close