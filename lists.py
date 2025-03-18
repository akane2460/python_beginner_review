# Python Tutorial for Beginners: Episode 6, Lists

# Lists are comprised of [] with any number of comma separated values
## from 1 to 6 manually
my_list1 = [1, 2, 3, 4, 5, 6]

## list integers from 1 to 5 (range does not include final integer)
# my_list2 = list(range(1, 6))
### range can take a 3rd argument, shows at what value it lists by
#my_list2 = list(range(0, 101, 10))
### range can only accomodate int values, not floats

#print(my_list1)
#print(my_list2)

# The type function tells you what type of variable it is (list, integer, string, float, etc.)
#print(type(my_list1))

# Operations on lists
print(my_list1[2]) # this returns the third element in the list
    # my_list[n] pulls the nth list number value in the list
print(my_list1[-1])
    # this pulls the last element in the list

# Create a slice from the second element
print(my_list1[1:])
    # if want to just slice from nth element to last can do list[n:]
    # if want to slice from n to x can do list[n:x]

# Get the length of a list
print(len(my_list1))

# Maximum and minimum of a list (highest # value and lowest # value)
print(max(my_list1))
print(min(my_list1))

# Add an element to a list
my_list1.append(120)
    # taking my_list1 and tacking on 120 to the end of the list
print(my_list1)

# Reverse a list
my_list1.reverse()
print(my_list1)

# Adding 2 lists together
my_list2 = [10, 20, 30, 40, 50, 60]

print(my_list1 + my_list2)
    # python doesn't add up the corresponding values for each nth element
        # it just tacks list 2 on the end of list 1
print(my_list2 + my_list1)