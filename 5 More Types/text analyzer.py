#defines function to count number of characters in a file
def counter(text, char):
    count = 0
    for x in text:
        if x == char:
            count += 1
    return count
#opens file and reads it
file_name = "C:\\Users\\tlee\\Documents\\Programming\\Python Serious Time\\5 More Types\\sample text.txt"
with open(file_name) as f:
    words = f.read()
#lowercases all letters since counting is case-sensitive
words = words.lower()
#since for loop goes through each item in a list, the string becomes a list where each character is an item in the list.
for char in "abcdefghijklmnopqrstuvwxyz ,.!?\n":
    #defines that the percent of a character is 100 times the number of times a character appears in the file
    #divided by the length of the file
    percent = 100 * counter(words, char)/len(words)
    #prints {0}: {1}% with 0 and 1 replaced with the character and percent rounded to the tenth space, respectively
    print("{0}: {1}%".format(char,round(percent,1)))