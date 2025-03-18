# Python Tutorial for Beginners: Episode 17 tuples

# What are tuples?
    # sort of look like lists, can store any data type
    # but cannot modify elements within them

# tuple example
fruit = ("Apples", 4, "Bananas", 5, "Oranges", 6)
print(type(fruit))

# can modify elements within a list
list_of_fruit = ["Apples", 4, "Bananas", 5, "Oranges", 6]
print(type(list_of_fruit))

list_of_fruit[0] = "Strawberries"

# can't modify elements within a tuple
# but we can perform similar operations on tuples

# slicing a tuple
print(fruit[0:3])

# concatenate tuples
fruit = fruit[:4] + ("Cherries", 10)
print(fruit)

# tuples with one element
x = (5, ) # this is notation for tuple with one element
print(type(x))

# length of tuple
print(len(fruit))

# creating a tuple
another_tuple = tuple(("Hello", 18, True)) # must have double () here
print(type(another_tuple))

# converting a tuple to a list and then back to a tuple
fruit = list(fruit)
fruit.append("Pears")
fruit = tuple(fruit)
print(fruit)

# unpacking tuples
fruit = ("Apples", "Bananas", "Pears", "Oranges", "Strawberries")
(one, two, three, four, five) = fruit
print(one) # variable one is assigned to "Apples"
print(two) # variable two is assigned to "Bananas"

fruit = ("Apples", "Bananas", "Pears", "Oranges", "Strawberries")
(one, two, *three) = fruit # the * assigns variable to a list of the remainder of the tuple
print(three)

# incoporating loops within tuples
for i in range(len(fruit)):
    print(fruit[i])
