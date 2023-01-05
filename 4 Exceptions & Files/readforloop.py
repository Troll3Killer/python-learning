#open command turns txt file into a list, with each line an entry in the list. r specifies read mode
file = open("C:\\Users\\tlee\\Documents\\Programming\\Python Serious Time\\4 Exceptions & Files\\testfile.txt", "r")
#for loop uses x as variable to do to each entry in a list (in this case each line) which is to print
for x in file:
    #because the open command adds an extra \n in the list, there is an extra space between each line ['Line 1\n', 'Line 2\n'...]
    print(x)
#closes the file with X.close command
file.close