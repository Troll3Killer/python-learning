import re
#string to be searched
cheese = "hello, I have a shell, and you can go to hell"
#regex search string
search = r"\b[hH][eE][lL][lL]\b"
#replace function with heck
colby = re.sub(search, "heck", cheese)
print(colby)