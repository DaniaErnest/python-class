# for Loops
# A for loop acts as an iterator in Python; it goes through items that are in a sequence or any other iterable item. 
# Objects that we've learned about that we can iterate over include strings, lists, tuples, and even built-in iterables 
# for dictionaries, such as keys or values.

# We've already seen the for statement a little bit in past lectures but now let's formalize our understanding.

# Here's the general format for a for loop in Python:

# for item in object:
#     statements to do stuff
# The variable name used for the item is completely up to the coder, so use your best judgment for choosing a 
# name that makes sense and you will be able to understand when revisiting your code. This item name can then be 
# referenced inside your loop, for example if you wanted to use if statements to perform checks.

# Let's go ahead and work through several example of for loops using a variety of data object types. We'll start 
# simple and build more complexity later on.

# We'll learn how to automate this sort of list in the next lecture
list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    print(num)

# Notice that if a number is fully divisible with no remainder, the result of the modulo call is 0. We can use this 
# to test for even numbers, since if a number modulo 2 is equal to 0, that means it is an even number!

# Let's print only the even numbers from that list!
for num in list1:
    if num % 2 == 0:
        print('even :',num)

# Another common idea during a for loop is keeping some sort of running tally during multiple loops. For example, 
# let's create a for loop that sums up the list:

# Start sum at zero
list_sum = 0 

for num in list1:
    list_sum += num
    #still the same like this
    # list_sum - list_sum + num

print('list_sum :',list_sum)

# We've used for loops with lists, how about with strings? Remember strings are a sequence so when we iterate through 
# them we will be accessing each item in that string.

for letter in 'Good Boy':
    print(letter)

# Let's now look at how a for loop can be used with a tuple:

tup = (1,2,3,4,5)

for t in tup:
    print(t)

# Tuples have a special quality when it comes to for loops. If you are iterating through a sequence that contains tuples, 
# the item can actually be the tuple itself, this is an example of tuple unpacking. During the for loop we will be unpacking the tuple inside of a sequence and we can access the individual items inside that tuple!

# a list of tuples
list2 = [(2,4),(6,8),(10,12)]
for tup in list2:
    print(tup)

# Now with Tuple unpacking!

for (t1,t2) in list2:
    print(t1)

d = {'k1':1,'k2':2,'k3':3}
it = d.items()
print(it)

# Dictionary unpacking
for k,v in d.items():
    print(k ,v)

# If you want to obtain a true list of keys, values, or key/value tuples, you can cast the view as a list:

viewAsList = list(d.keys())
print(viewAsList)

# Remember that dictionaries are unordered, and that keys and values come back in arbitrary order. 
# You can obtain a sorted list using sorted():

sortValue = sorted(d.values())
print(sortValue)