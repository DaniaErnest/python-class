# Tuples
# In Python tuples are very similar to lists, however, 
# unlike lists they are immutable meaning they can not be changed. 
# You would use tuples to present things that shouldn't be changed, 
# such as days of the week, or dates on a calendar.

# In this section, we will get a brief overview of the following:

# 1.) Constructing Tuples
# 2.) Basic Tuple Methods
# 3.) Immutability
# 4.) When to Use Tuples

# You'll have an intuition of how to use tuples based on what you've learned about lists.
#  We can treat them very similarly with the major distinction being that tuples are immutable.

# Constructing Tuples
# The construction of a tuples use () with elements separated by commas. For example:

# Create a tuple
t = (1,2,3)
# Check len just like a list
len(t)
3
# Can also mix object types
t = ('one',2)
print(t)

# Use indexing just like we did in lists
print(t[0])
# Slicing just like a list.. this [-1] print from back
print('slice :',t[-1])

# Basic Tuple Methods
# Tuples have built-in methods, but not as many as lists do.
#  Let's look at two of them:

# Use .index to enter a value present in the tuple and return the index
ind = t.index('one')
print('inde :',ind)


# Use .count to count the number of times a value appears
ty = t.count('one') #1
print('count :',ty)


# Immutability
# It can't be stressed enough that tuples are immutable. 
# To drive that point home:

# t[0]= 'change'
# print(t)

