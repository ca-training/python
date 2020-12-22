s = "All that glitters is Gold"
print(s)

# strings are sequences
length = len(s)
print("Length of the string is {} characters".format(length))

# simple transformation methods
print(s.upper())

print(s.lower())

print(s.replace("is", "is not"))

# string methods do not change the original string
a = s.replace(" ", "")
print(s)
print(a)

# split and join
wordlist = s.split()
print(wordlist)

separator = ","
csvline = separator.join(wordlist)
print(csvline)

wordlist = csvline.replace(",", "|").split("|")
print(wordlist)

# splitlines is a cross-platform way to separate lines
multi = """multi
line
string"""
print(multi.splitlines())

# strip
fat = " whitespace "
lean = fat.strip()
print("Strip converts '{}' to '{}'".format(fat, lean))

# strip is strong
messy_string = " \n, \n some useful information \n ;\t "
clean_string = messy_string.strip(",;\t\n ")
print("'" + clean_string + "'")

# all the indexing and other sequence goodness works...
print("Indexes from s: " + s[4] + s[10:12] + s[-1])
# an element of a string is a ... string
print(type(s[2]))

# characters and ordinals
cipher = ""
for c in s:
    cipher += chr(ord(c) + 1)
print("The code is: " + cipher)

message = ""
for c in cipher:
    message += chr(ord(c) - 1)
print("Decoded: " + message)


# better formatting
fmt = "{item} : ${price:7.2f}-"
print(fmt.format(price=33.3453, item="fan"))
print(fmt.format(price=1012.1, item="cpu"))

# also, this is a thing...
repetitive = "foobar" * 9001  # foobarfoobarfoobarfoobarfoobarfoobar... etc.
# print(repetitive)
