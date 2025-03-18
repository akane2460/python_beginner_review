# Python Tutorial for Beginners: Episode 14 Python Types and Logicals

# basic types in python
print(type("Hello World!")) # string
print(type(13)) # int
print(type(4.72)) # float
print(type(True)) # bool

## commands to change types
# changing to int
print(4.72, int(4.72))
print(4.05, int(4.05))
    # python rounds down to the floor with int()
print(4.72, int(round(4.72)))
    # round() follows standard rounding rules

# changing strings to integers
print("12345", int("12345"))
print(type("12345"), type(int("12345")))
    # cant change string to int if letters involved

# changing to floats
print(float(12))
print(float("12345"))

# changing to strings
print(str(18))
print(str(129.5))
print(type(str(129.5)))

## logical operators
# three different logical operators: 'and' 'or' 'not'
x = 6
print (x > 0 and x < 10)

y = 24
print(y % 2 == 0 or y % 3 == 0)