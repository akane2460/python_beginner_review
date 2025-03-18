# Python Tutorial for Beginners: Episode 15 Strings

# Already covered strings, int, floats, bools and lists

# Integers, floats, bools all simple data types
    # cannot be broken down

# Lists and strings different-- made up of smaller pieces
    # CAN be broken down

# already know what strings are
print("Hello, world!")
print(type("Hello, world!"))

# operations on strings
# + operator: concatenation
greeting = "Hello"
name = "Ellie"
print(greeting + name)

# * operator: multiples strings together
print(greeting*3)
print((greeting + name)*3)

# index operator: pull out specific character in string
name = "Brad"
print(name[0])
print(name[0] + name[3])
# slicing strings
print(name[0:2])
print(name[:2])
print(name[2:])

# lowercase and uppercase
name = "Ellie"
print(name.lower())
print(name.upper())

# count number of identified characters in string
print(name.count("l"))

# replace specific characters with other characters
print(name.replace("l", "d"))

# finding length of string
print(len(name))

# format strings
# your_name = input("Your name: ")
# hello = "Hello {}".format(your_name)
# print(hello)

# Each letter in python is assigned to a specific number!
    # so can do math with strings
print("orange" < "strawberry")
print(ord("O")) # capital O = 79
print(chr(78)) # capital N = 78

# is and not opeartors
fruit = "banana"
print("a" in fruit)
print("s" not in fruit)

# overall summary
x = "hello"
y = ""
for character in x:
    y = y + character.upper()
print(y)
