# open, read, write
# (todo)

# try, except
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
infinite_loop = True
try:
    a = 0
    while infinite_loop:
        a += 1
except KeyboardInterrupt:
    print("\nctrl-c was pressed, good thing too...\n")

# ProTip: There's no point catching an exception if
# all you're going to do is print an error and exit
# that is what the exception does when uncaught...
