# Python Tutorial for Beginners: Episode 18 Basics Review + Quiz

# Q1 Variables
x = 2
y = 4
print(x + y) # addition
print(x / y) # division
print(x - y) # subtraction
print(x * y) # division

# Q2 Lists
# List of 0 to 100 with all even numbers
list_1 = list(range(0, 101, 2))

# Print first 10 elements of list
print(list_1[:10])

# Find the length
print(len(list_1))

# Append any value onto the list
list_1.append("z")
print(list_1[51])

# Q3 If statements
# Assign variable to any integer you want
# using if statement, find if divisible by 5 (print if is or not)
var = 25
if var % 5 == 0:
    print("It is divisible by 5")
else:
    print("It is NOT divisible by 5")


# Q4 For Loop
# Using for loop, get python to print numbers 0 to 5

for i in range(0, 6):
    print(i)

# Q5 Turtle
# Can you draw a pentagon
import turtle
turtle.forward(30)
turtle.left(72)
turtle.forward(30)
turtle.left(72)
turtle.forward(30)
turtle.left(72)
turtle.forward(30)
turtle.left(72)
turtle.forward(30)
turtle.left(72)

# Q6 Functions
# Create a function that tests whether numbers (a, b, c) are pythagorean triple

def function(a, b, c):
    if a**2 + b**2 == c**2:
        result = True
    else:
        result = False
    return print("These make a triple, True or False?", result)

# Q7 While loop
# Spot the error in this code:
    # n = 5
    # while n > 0
    # n = n + 1
        # print(n)
# The error is that the while loop is lacking a colon and needs second line to be indented
# n = 5
# while n > 0:
#     n = n + 1
#     print(n)

# Q8 Matplot lib
# Plot 2 lists of length 5 or more against each other using matplot lib
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.show()