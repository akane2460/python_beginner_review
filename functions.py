# Python Tutorial for Beginners: Episode 12 Functions

# like in math, where a function takes an argument and produces a result
# it does so in Python as well

# The general form of a Python function is:
# def function_name(arguments):
#   {lines telling function what to do to produce the result}
#   return result

# Let's consider producing a function that returns x^2
def squared(x, y):
    result = x**2 + y**2
    return result

print(squared(2, 8))

# A new function
def born(country):
    return print("I am from " + country)

born("Canada")
born("El Salvador")
born("The US")