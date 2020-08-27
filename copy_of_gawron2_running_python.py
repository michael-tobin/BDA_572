# -*- coding: utf-8 -*-
"""Copy of gawron2_running_python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/gawron/python-for-social-science/blob/master/intro/running_python.ipynb

Note:  If you are looking at this notebook on github and wondering how on earth to run it have a look [at this section of the online book](https://gawron.sdsu.edu/python_for_ss/course_core/book_draft/Introduction/starting_up_python.html).  Bear in mind you'll not only need to download the "Open in colab" extension of your Chrome browser.  You'll also need to be logged in to your Google account.

# Running python

The first command in the cell below will start off many notebooks.  It loads matplotlib (graphing) tools and numpy (extended math) tools into Python.  It also guarantees your plots will appear in the notebook rather than in a separate window.
"""

# Commented out IPython magic to ensure Python compatibility.
# %pylab inline

total_secs = 7684
hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes =  secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining  % 60

"""If youve just loaded this notebook, you might want to run the commands in the cell above.  This is done by placing your cursor in the cell and hitting the enter key **while** holding down shift, which we will henceforth write as `[Shift]`-`[Enter]`.  After you do that the 5 variables will have the values they were assigned in the cell."""

total_secs  + 1

hours

minutes

secs_still_remaining

secs_finally_remaining

"""To look at the values of a set of variables you can do what we just did, typing each variable to Python, but there are some other options.  One is to type a tuple to Python, to look at several variables at once."""

(total_secs, hours, minutes, secs_still_remaining,secs_finally_remaining)

"""Another is to use Python's print statement."""

print("Hrs =", hours, "mins =", minutes, "secs =", secs_finally_remaining)

"""Some important features of the `print` statement are illustrated.  `print` takes any number of arguments, separated by commas.  The commas are interpreted as spaces.  The final argument is not followed by a comma so print adds a newline character ("\n").  The syntax of `print` is like nothing else in Python (no parens), and has been changed in Python 3.0, so this is how we'll be using it.

# Python arithmetic

Lets look at each of the lines in the code and see what it computes.  Python has two division operators, '//' and '/'. This is illustrated in the next line.
"""

total_secs // 3600

"""Note that even though the value of *total_secs* is 7684, the value returned is an integer.  The '//' operator always rounds off to the nearest integer when necessary."""

7200.1//3600

"""The '%' operator (also called the **modulus** operator) computes the *remainder* in a division."""

total_secs % 3600

345.3 % 3

"""## Basic arithmetic

Multiplication
"""

3 * 2

"""Addition"""

3 + 2

"""Subtraction"""

3 - 2

"""Raising to a power"""

3 ** 2

"""Taking the log.  The next line is log of 3."""

log(3)

"""In regular Python, this would be a `NameError` because the *log function* is not one of the builtin Python math functions.  But because we executed `%pylab` when we started up this notebook, all the extended math functions defined in the `numpy` module are defined.  One of those is `log`.  As an example of some possible pitfalls, we'll compare this `log` with the more vanilla version from the standard Python `math` module.  `math.log` does give the same answers for real numbers."""

import math
math.log(3)

"""By default, math.log does natural logarithms, as does `numpy.log`, so if you dont specify the base, it is **e**.  But unlike the numpy implementation, `math.log` lets you choose other bases."""

math.log(3,2)

"""Trying this with the `numpy.log` raises an exception.  `numpy.log` does take a second argument but it's used for purposes we won't delve into right now."""

log(3,2)

from math import e
math.log(e)

e

math.log(4)

math.log(4,2)

"""The numpy version of log is pretty geeky. For example, it's defined for complex numbers."""

log(3+2j)

"""The regular Python version of log is not."""

math.log(3+2j)

"""The Python *math* module is very spare and lacks a number of important mathematical tools of interest to data scientists.  Later on in this course we will be introduced to the more complete set of tools available in the *numpy* module.

## Student confirmation section

Evaluate the cell below, to find out the value of the expression.
"""

from math import pi
pow(e,(0+1j)*pi)

pow(e,(1j*pi))

log(-1+0j)

"""# Textbook problems

Recall the first cell in this notebook.
"""

total_secs = 7684
hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes =  secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining  % 60

"""Each of these 5 lines involves assigning a value to a **name** or **variable**.  Pythonistas use both terms (there is a slight technical difference that needn't worry us now).  For example, the first line assigns the value 7684 to the **name** `total_secs`.  The second line assigns whatever you get by dividing `total_secs` by 3600 to the name `hours`. And so on.

Above, we printed out information about all the above computations as follows:
"""

print("Hrs =", hours, "mins =", minutes, "secs =", secs_finally_remaining)

"""There's a somewhat cooler way to do the same thing that looks like this:"""

print(f"Hrs = {hours} mins = {minutes} secs = {secs_finally_remaining}")

"""When we print the string, the bracketed names `{hours}`, `{minutes}` and `{secs_finally_remaining}` are all replaced with the values of the names. For this to work, the names have to have been given values beforehand (as we did above), and we have to tell Python that this is a special kind of string that has variable slots by prefixing the string with "f".  Not surprisingly, these kind of strings are called **f-strings**.

**Exercise 1**. For your first exercise, use the cell below. Use a variable to represent a person's name, and print a message to the person using an f-string.  For example the name might be Bozo and the message might be "Hey Bozo, you're pants are on fire!"
"""

name = "Bozo"
print(f"Hey {name}, your pants are on fire!")



"""Your second exercise will make use of the string methods `title`, `upper` and `lower`, illustrated below:"""

alphabet = 'abcdefghijklmopqrstuvwxyz'
sentence = 'The quick brown fox jumped over the lazy yellow dog.'

print(alphabet)
print (alphabet.title())
print(alphabet.lower())
print(alphabet.upper())
print()
print(sentence)
print (sentence.title())
print(sentence.lower())
print(sentence.upper())

"""**Exercise 2**.
In the next cell, use a variable to represent a person's name and print that name in lower case, upper case, and title case.  Be sure to use f-strings.
"""



"""**Exercise 3**.  Find a quote whose source you know and print the quote and the name of its author.  For example, as a particularly challenging example, you might want to print out

```
"There's a sucker born every minute," P. T. Barnum once said.
```
Your answer should go in the next cell.  To understand how to create a string with quotes inside it, you might need to look at [the introduction to strings in the online textbook.](https://gawron.sdsu.edu/python_for_ss/course_core/book_draft/Python_introduction/python_types_first_pass.html#strings)
"""



"""For your next exercise, you'll make use of some Python methods that trim white space (space, tab, newline) off strings.  These are illustrated below.  First `rstrip`:"""

X = "fred"
print(X)
Y = "fred "  # add an extra space at the end ...
print(Y)  # Looks deceptively just like printing X, BUT
print("X == Y: ", X == Y, " len X:",len(X), "len Y:", len(Y))
Z = Y.rstrip()  # Now strip away white space on the right.
print("X == Z: ", X == Z, " len X:",len(X), "len Z:", len(Z))

"""Now the mirror image method, `lstrip`:"""

X = "fred"
print(X)
Y = " fred"  # add an extra space at the beginning ...
print(Y)  # This time X and Y print out differently
print("X == Y: ", X == Y, " len X:",len(X), "len Y:", len(Y))
Z = Y.lstrip()  # Now strip away white space on the left.
print("X == Z: ", X == Z, " len X:",len(X), "len Z:", len(Z))

"""Now a convenient variant that strips white space on both the right and left sides, a very frequently used method in text preocessing."""

X = "fred"
print(X)
Y = " fred "  # add an extra space at the beginning and at the end...
print(Y)  # X and Y print out differently
print("X == Y: ", X == Y, " len X:",len(X), "len Y:", len(Y))
Z = Y.strip()  # Now strip away white space on both sides.
print("X == Z: ", X == Z, " len X:",len(X), "len Z:", len(Z))

len(Z)

"""**Exercise 4**.  In the next cell, use a variable to represent a person's name and include some white space both before and after the name.  Print the name once so the white space around the name is displayed.  Then print the name using each of the three stripping functions `lstrip`, `rstrip`, and `strip`."""



