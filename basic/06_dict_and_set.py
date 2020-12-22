# the set - an -unordered- collection of -unique- values
bowl = {"apple", "banana", "pear"}
for fruit in bowl:
    print(fruit)

# enforces deduplication when created from a list
contents = ["apple", "banana", "pear", "grape", "grape", "grape"]
print(contents)
bowl = set(contents)
print(bowl)

bowl.add("mango")
bowl.remove("apple")  # this raises an error if it isn't there
# bowl.remove("apple") # KeyError
bowl.discard("grape")  # remove if it exists
bowl.discard("grape")  # don't complain if it isn't there

# set operations
# A.union(B) (A ⋃ B)
# A.intersection(B) (A ⋂ B)
# A.difference(B) (A - B)
# A.issubset(B) ? (A ⊆ B)
# A.issuperset(B) ? (A ⊇ B)

# Exercise: write a function that takes two parameters
# and returns their multiplication
# if either parameter is a type other than float or int
# it should return None
# (hint: sets are fun)


# dict - a.k.a map, a.k.a hashtable

employee = {
    "name": "timmy",
    "age": 8,
    "pay": 3.5,
    "competencies": ["python", "c", "excel"],
    42: "yes",
    1.0: "allowed",
}

print(len(employee))

print(employee["name"])
print(employee[42])

# print(employee["notakey"]) # this would raise a KeyError
print(employee.get("notakey2"))
print(employee.get("notakey2", "defaultval"))

for key in employee:
    print("  - " + str(key) + " : " + str(employee[key]))

# a dictionary has various 'views' which can be interpreted as collections
print(employee.keys())
print(employee.values())
print(employee.items())

# an assignment is not a copy
e2 = employee
e3 = e2.copy()

# equality is not identity
print(e2 == employee)
print(e2 is employee)
print(e3 == e2)
print(e3 is e2)

# Exercise:
#  1. Create a set with 1000 Fibbonacci numbers
#  2. Create a dictionary with:
#           a. keys as digits 0-9
#           b. values as occurence count of the digit in the set of numbers
#  3. Print the dictionary

# Review:
# https://www.w3schools.com/python/default.asp
# From intro up to and including functions
