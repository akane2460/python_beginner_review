# Python Tutorial for Beginners: Episode 11 Booleans, More loops and Statements

# Booleans
print(type(True)) # bool
print(type("True")) # str

# practice with bools: if testing statement correct
# print (5 == 5)
# print(6 == 5)

# incorporating the if statement with a boolean
x = 11
y = 5
if x % y == 0:
    print(True)
else:
    print(False)

# while loop
number = 1
while number < 4:
    print(number)
    if number == 4:
        break
    number = number + 1

# using else in a while loop
number = 2
while number < 4:
    print(number)
    number = number + 1
else:
    print("Number is no longer < 4")

# if statement
number = 1
if number > 0:
    print("Positive Number")
elif number == 0:
    print ("Zero")
else:
    print("Negative Number")