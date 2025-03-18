# Python Tutorial for Beginners: Episode 5, Basic Operations
## Load packages
from math import sqrt
from math import factorial

## print a string (letters, phrase, etc.) MUST be in quotes
print("Hello, world!")

## assigning variables with =
Hello = 2
print(Hello) # this will print the variable Hello
x = 91274 * 8
y = 200
print(x) # this will print the variable x
print(y) # this will print the variable y
print(x,y) # this will print the variables x and y
### python runs in order, so if Hello definition is below print command,
### won't work. MUST assign variable before using it

# More complex Math
number = 4
# square root of number (operation for power is **)
print(number**0.5)
# alternative way to perform square root of number
print(sqrt(number)) # must load package math and call the function at top of the document

# Factorials
# written out way 5! = 5 * 4 * 3 * 2 * 1
print(5 * 4 * 3 * 2 * 1)
# using factorial() function from math package
print(factorial(50))

# BASIC OPERATIONS (listed)
    # + is addition
    # - is subtraction
    # * is multiplication
    # / is division
    # ** is to the power of _
    # % is modulus (the remainder of a division expression)
    # sqrt() from the math package is square root
    # factorial() from the math package is factorial