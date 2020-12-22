#
# file io
#

my_file_path = "file.txt"
my_file = open(my_file_path, "w")

my_file.write("this file has content\n")
my_file.write("we wrote it\n")

my_file.close()

# opening with "w" will truncate the file, "a" appends
my_file = open(my_file_path, "a")

my_file.write("and another thing...\n")

my_file.close()

# opening for reading is "r" (this is the default)
my_file = open(my_file_path, "r")
content = my_file.read()
print(content)

# additional flags
# "+" - both reading and writing
# "x" - exclusive creation, fail if file exists
# "b" - binary mode
# these can be combined (i.e. "+")

my_file = open("foo.bin", "x+b")

my_file.write(bytes(34))

my_file.close()


# closing files is a drag
with open("selfclosing.txt", "w") as f:
    f.write("carefree\n")
    f.write("nonchalant\n")
    f.write("unphased\n")
    f.write("work smarter not harder\n")

# files are 'iterable'
with open("selfclosing.txt") as f:
    for line in f:
        sentence = line.strip()
        print(sentence)

#
# try, except
#

try:
    with open("nonexistentfile") as f:
        print("wow that worked!")
except Exception:
    print("hmm, no that didn't work")

# more specific exceptions can be caught individually
try:
    with open("nonexistentfile") as f:
        print("wow that worked!")
except FileNotFoundError:
    print("file not found")
except IsADirectoryError:
    print("uh, that's actually a folder...")


# and example of catching an interrupt coming out of a loop
# (change the False to True)
infinite_loop = False
try:
    a = 0
    while infinite_loop:
        a += 1
except KeyboardInterrupt:
    print("\nctrl-c was pressed, good thing too...\n")

# ProTip: There's no point catching an exception if
# all you're going to do is print an error and exit
# that is what the exception does when uncaught...


#
# import
#

# the import statement brings modules into scope
# once in scope, elements of the module (like functions or object)
# can be used.

# Lets download a file from the internets
import urllib.request

imgurl = "https://imgs.xkcd.com/comics/python.png"
imgcontent = urllib.request.urlopen(imgurl).read()

imgfile = "python.png"
with open(imgfile, "wb") as f:
    f.write(imgcontent)

# also acceptable:
from urllib import request
from urllib.request import urlopen

# Homework
# 1. Download and save Charles Dickens' A Tale of Two Cities from:
# https://www.gutenberg.org/files/98/98.txt
# 2. Build a word frequency scoreboard of 25 most common words
# 3. Build a word frequency scoreboard of 25 most uncommon words
# 4. Calculate average occurence of top 25 words
# 5. Calculate average occurence of bottom 25 words
# (bonus points) 6. Calculate variance/stdev of occurence
# (weekend quarantine is boring) 7. Do it all with minimum cpu/memory use
#
# All code must be properly commented and formatted
#