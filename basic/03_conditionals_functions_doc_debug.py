# if and indenting
the_thing = True
the_other_thing = False

if the_thing:
    print("the thing")  # whitespace indent defines the body
elif the_other_thing:
    print("the other thing")
else:
    print("nothing")

# numeric conditionals
a = 13
if 10 <= a <= 17:
    print("a is between 10 and 17")

if the_thing and the_other_thing:
    print("All the things")

if the_thing or the_other_thing:
    print("at least one of the things")

# false-y things evaluate to false
from pprint import pformat

for a in [0, 17, 0.0, 102.5, "", "foo", "0", None]:
    print("{} evaluates to {}".format(pformat(a), bool(a)))


# functions are defined like so...
def a_func():
    print("This function does stuff when it is called...")


# we add parentheses to call a function
a_func()

# Exercise: write a function that prints "Hello World"

# talking about scopes with a function that does nothing...
def useless_func():  # any line ending with ':' creates a new scope
    # each subsequent scope must be indented by whitespace
    # (your linter/styler should catch bad indentation)
    # (but if it doesn't the interpreter certainly will...)
    # python does not allow empty scope bodies
    # so we use the special 'pass' keyword to define a 'no operation' scope
    pass


# functions may have parameters and can return things
def the_func(param):
    print("we got the_func... ")
    return type(param)


# we call functions with params as you might
print(the_func(5.2))

# Exercise: write a function that returns a string describing the type of the parameter

# basic types are passed by value
def print_plus_one(x):
    x += 1
    print(x)


x = 5
print_plus_one(x)
print(x)

# multiple parameters work as you might expect
def greeting(name, surname):
    print("Hello " + name + " " + surname)


# thus giving us the standard positional argument calling convention
greeting("Can", "Aydin")

# but you can also specify keyword arguments, which are NOT positionally bound
greeting(surname="Bond", name="James")

# default parameter values are fairly straightforward
def circle_area(radius=1):
    return 3.14 * (radius ** 2)


# Exercise: write a function that calculates distance of a cartesian point from the origin and defaults to (1 , 1)

# runs with default value
print(circle_area())
# or with given value
print(circle_area(2))

# with multple values we use newlines for readability
def greet(
    name="Mr",
    surname="Bond",
    exclamation="Hello",
    pleasantry="I'm very pleased to meet you!",
):
    print(exclamation + " " + name + " " + surname + ", " + pleasantry)


# Exercise: write the previous function on one line, then run black on the file


# overriding is simple
greet("Fuzzy", "Bear")

# and you can just replace by keyword
greet(pleasantry="I expect you to die...", exclamation="No")


# functions should be documented
def user_friendly(x):
    """! if a function is part of a module, it should be documented with
    a comment like this one explaining what it does and usage if needed
    your editor will hopefully find and show the user this text on mouseover.

    so try and make it helpful

    maybe even add some doxygen markup (enabled by the '!' syntax above):

    @param x a numeric type that the function will double

    @return two times x...
    """
    print("my_func is funky")
    return x * 2


x = 2
y = user_friendly(x)


# functions are also a type, and can be assigned like any other
f = user_friendly
# note that we are -not- calling the function, but creating an alias for it...
print(type(f))
a = f(2)
print(a)

# to make sure your formatting is up to spec run 'black' with the source file or folder
# alternatively 'Format Document' in vscode right-click context menu
# for just checking: black --check <path>

# debugging - press f5
# if it asks select 'python file ...'
# in the debug configuration window, click on 'create a launch.json file'
# and select 'python file ...' again

# write a (buggy) function
def cube(a):
    b = a * 2
    return b


# call it
c = 4  # set a breakpoint here... and hit f5
d = cube(c)
print("Is {} equal to {}?".format(d, c ** 3))
# use the debugger to step through the function
