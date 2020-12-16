#
# the list - an ordered collection of elements
#
groceries = ["milk", "butter", "chainsaw"]
print(groceries)

# indexable
print(groceries[0])
# N.B. python, like all other -normal- computing languages, starts counting at 0

# negative indexes work from the end
print(groceries[-2])

# if an index exists, it can be set by assignment
groceries[2] = "bread"
print(groceries)

# len gives length
cart_size = len(groceries)
print(cart_size)

# add to the end
groceries.append("rice")
print(groceries)

# insert in the middle
groceries.insert(1, "coffee")
print(groceries)

# remove by value
groceries.remove("butter")
print(groceries)

# type agnostic
stuff = ["inception", 2010, True, 8.8, "", ["chris", "nolan"], None]
print(stuff)
print(len(stuff))
print(len(stuff[5]))

# pop last item
end = stuff.pop()
print(end)
print(stuff)

# pop first (or any indexed) item
start = stuff.pop(0)
print(start)
print(stuff)

# lists are passed to functions by reference
def change(x):
    x[0] += 1


x = [2, 4]
change(x)
print(x)

# however, assigning within a function creates a new list
def trytodouble(x):
    x = x + x  # a new list is created and assigned here
    return x  # if we don't return it, the new list never gets out


y = trytodouble(x)
print(x)
print(y)

# assigning inside a function creates a new list


#
# lists are our first type that can be:
#

# iterated
for item in groceries:
    print(item)

# queried for elements
if "coffee" in groceries:
    print("all nighter")

if "bread" not in groceries:
    print("do we have cake?")

# concatenates
print([1, 2, 3] + [4, 5, 6])

# sliced
print(groceries[1:4])

# sliced with steps
print(stuff[0:7:2])

# min and max
histog = [2.2, 4.7, 12.0, 17.0, 9.0, 1.0, 0.0, 1.0, 2.2, 3.0, 4.0]
print("min of {} is {}".format(histog, min(histog)))
print("max of {} is {}".format(histog, max(histog)))

# count occurences
groceries.append("rice")
print(groceries.count("rice"))

# finding the index of an element
print(groceries.index("rice"))
# after 1
print(groceries.index("rice", 4))
# after 2 but before 4
print(groceries.index("rice", 1, 4))

#
# tuple - an immutable ordered collection
#
essentials = ("milk", "butter", "chainsaw")
print(essentials)

# it can be constructed from a list
essentials = tuple(groceries)
print(essentials)

# shorthand assignment for functions returning tuples
quotient, remainder = divmod(13, 5)
print((quotient, remainder))  # (2, 3)

# to create a tuple from a single value, add a comma
# this useful for concatenating a tuple with a single value
# a = (4, 5) + 6 # this fails
a = (4, 5) + (6,)
print(a)


#
# the range - an immutable regular sequence
#
for i in range(10):
    print(i)

for i in range(1, 6):
    print(i)

# a third argument specifies the step
for i in range(0, 30, 5):
    print(i)

# a negative step allows counting down
for i in range(5, -5, -1):
    print(i)

# the traditional for loop is built with ranges
for i in range(len(groceries)):
    print(groceries[i])

# Exercise: create and print a list of the first 20 fibbonacci numbers
# Where Fib(0) = 0, Fib(1) = 1, Fib(n) = Fib(n-1) + Fib(n-2)
