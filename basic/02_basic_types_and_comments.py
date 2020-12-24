# you'll notice we are commenting by starting lines with the '#' character

# strings are pretty straightforward
message = "have a nice day"
print(message)

message = "double quotes are exaclty the same as single quotes"
print(message)

message = 'which means you should never need a backslash (\\) to escape "quoted" string content'
print(message)

message = 'I mean you "could" do it but nobody will "like" you...'
print(message)

# newlines and other special chars are similar to most other languages
divider = "\n----\n"
print(divider)

# what is the type of this variable?
# N.B. 'type()' is a built-in language function ... that returns type...
print(type(message))

print(divider)

# what type is type?
print(type(type(message)))

print(divider)

# other ways to declare literal strings
message = "double quotes are also fine"
print(message)
print(type(message))

print(divider)

# multi-line strings are a thing
message = """roses are red,
violets are blue,
multi-line strings,
are sometimes useful"""
print(message)
print(type(message))

print(divider)

print(
    """you can actually use multi-line strings
as multi-line comments..."""
)

"""since the interpreter will ignore unassigned strings,
it is a comment for all practical purposes..."""

print("and you can " + "'add'" + " strings to each other to concatenate them")

print(divider)

# types are defined by assignment, lets create an int
x = 12

# all built-in types can be printed
print(x)
print(type(x))

# simple arithmetic
t = 2 * x - 4
print(t)

print(divider)

# you can operate on the fly
print(3 * x + 1)
print(x / 3)

# there's a short hand to increment/decrement (also works for *,/)
x += 3
print(x)
x -= 3
print(x)

# integer division is //
print(x // 5)

# modulo (remainder) operator is %
print(x % 5)

# powers can be calculated using (base ** exponent)
print(x ** 2)
print(2 ** x)

print(divider)

# now a rational number
y = 2.71828
print(y)
print(type(y))

# float precision is limited to around 1e-16 (see the decimal type for more)
y = 2.7182818284590452

# rounding is pretty simple
print(round(y))

# rounding to n decimal places
max_precision = 2
rounded = round(y, max_precision)
print(rounded)

print(divider)

# why would anyone want a scripting language that has built-in support for complex numbers?
z = complex(3, 1)
print(z)
print(type(z))

print(divider)

# type is dynamically decided at assignment, so what might be the type of x at print(x) ...?
x = (x + y) * z
print(x)
print(type(x))  # (do I even care?)

print(
    """ProTip: NEVER force the reader to think about operator precedence,
 ALWAYS use parenthesis!"""
)

print(divider)

# boolean types exist
p = True
print(p)
print(type(p))


# python syntax is quite ... straightforward
q = not p
print(q)
print(type(q))

print(divider)

# you can explicitly cast one type to another
result_str = str(p ^ q)  # xor
print("The result is: " + result_str)
type_str = str(type(result_str))
print("The type of the result is: " + type_str)

# we can get smarter with printing strings using str.format
formatted_str = "nand({}, {}) evaluates to {}"
print(formatted_str.format(p, q, not (p and q)))

# casting a float to int will always round down (floor)
n = int(y)
print("casting {} to {} is {}".format(y, type(n), n))

print(divider)

# looking into the void:
print(None)
print(type(None))
print(bool(None))


print(divider)

# lastly, 'print()' IS NOT your friend
a = 5
b = "5"
#
# .... a thousand lines of code and several files later ...
#
if not a == b:
    print("a is not equal to b, see below:")
    print("a is {}".format(a))
    print("b is {}".format(b))
    print("See? They are different!")

print(divider)

# pretty-print IS your friend
from pprint import pprint

pprint(a)
pprint(b)
pprint("We are done here...")
