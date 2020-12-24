# Introduction to Python

## Getting Started

This intro assumes a basic understanding of procedural programming including
statements, variables, assignments, arithmetic, conditionals, loops and scope.
Proficiency in object oriented coding and data structures will help, but is not
required.

There are many python programming environments (like, seriously, a lot),
native/python/pip/pylint/vscode has been selected as it is a popular and
lightweight cross-platform combination that is easy to set up yet does not
obscure too much of the 'vanilla' way of doing things.

It is also what our team uses at the moment...

There are many other environments, if you are able to nitpick about virtualenv
vs conda vs whatever, you are probably already beyond the scope of at least
half of the material here.


### Install prerequisites

This section should be completed prior to starting the training modules

#### Note on Python version 3 vs 2

Support for Python version 2 officially ended on 2020-01-01.

From here on out, all references to Python will mean Python version 3.

Python 3 and Python 2 are not fully compatible, so in order to protect
the space-time continuum please make sure to actively avoid
any and all Python 2 examples, modules, binaries or tools.


#### Windows
1. Download and run:
    https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe
2. In the first screen check **"Add Python 3.9 to PATH"**
3. Click "Install Now"
4. Feel free to disable the 260 character path limit
5. run the installer
6. open a command prompt and use pip to install ipykernel, pylint and black
    1. `C:\Users\can.aydin>pip install ipykernel`
    2. `C:\Users\can.aydin>pip install pylint`
    3. `C:\Users\can.aydin>pip install black`
7. Install vscode https://code.visualstudio.com/download
8. Open vscode and install Microsoft Python extension https://marketplace.visualstudio.com/items?itemName=ms-python.python

#### Linux
1. Install python (version 3), pip, pylint, ipykernel with the package manager of your distro.

    i.e.: for ubuntu 20.04 this might look like:
    ```
    sudo apt install python-is-python3 python3-pip && pip3 install pylint && pip3 install ipykernel && pip3 install black
    ```
2. Install vscode https://code.visualstudio.com/download
3. Open vscode and install Microsoft Python extension https://marketplace.visualstudio.com/items?itemName=ms-python.python

### Follow a simple python tutorial

https://code.visualstudio.com/docs/python/python-tutorial

## Python Basics

### Hello World

1. Setting up the editor
2. Working with the python interpreter
3. Running a script from file

### Basic Types and Comments

1. Strings
2. Integers and basic arithmetic
3. Floats, rounding, a complex number
4. Dyanmic types
5. Booleans and logical operators
6. Type casting and str.format()
7. Pretty print

### Functions, Coding Style and Debugging

1. Conditionals and boolean evaluation
2. Defining and calling functions
3. Scope and indentation
4. Parameters and return values
5. Documentation and doxy markup
6. Functions as types
7. Style checking with black
8. Single script debugging with vscode

### List, Tuple, Range

1. List
2. Tuple
3. Range

### String Operations

1. Transformations
2. Splitting and joining
3. Strings as sequences
4. Unicode ordinals
5. Formatting

### Set and Dict

1. Set
2. Dict

### File I/O and Exceptions

1. Open
2. Read
3. Write
4. Try-Except
5. import

### TODO

* Classes
* Inheritance
* Delete
* Binary data
* Iterators
* Lamdas
* Comprehension
* Modules
* Dates & Logging
* JSON
* Regex

