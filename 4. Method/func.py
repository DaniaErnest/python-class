def say_hello ():
    print('hello')

say_hello()

# Accepting parameters (arguments)
# Let's write a function that greets people with their name.
def greetings(name):
    print(f'hello {name}')
    print('hello {}'.format(name))

greetings('Segun')

# Using return
# Let's see some example that use a return statement. return allows a function to 
# return a result that can then be stored as a variable, or used in whatever manner a user wants.
def addnum(a,b):
    return a + b
    
sum = addnum(1, 2)
print(sum, 'and', sum+sum)

# Adding Logic to Internal Function Operations
# So far we know quite a bit about constructing logical statements with Python, such as if/else/elif statements, 
# for and while loops, checking if an item is in a list or not in a list (Useful Operators Lecture).

# Check if a number is even
# Recall the mod operator % which returns the remainder after division, 
# if a number is even then mod 2 (% 2) should be == to zero.

print(20 % 2 == 0, 'and', 21 % 2 == 0)

def even_check(number):
    return number % 2 == 0

check = even_check(21)
print(check)

# Check if any number in a list is even
# Let's return a boolean indicating if any number in a list is even. 
# Notice here how return breaks out of the loop and exits the function

def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            # return number     # We can return the umber that gives the true
            return True
        # Otherwise we don't do anything
        else:
            pass

che = check_even_list([1,2,3])
print('truth :',che)

# We need to initiate a return False AFTER running through the entire loop**

def check_even_list(num_list):
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we return True
        if number % 2 == 0:
            return True
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return False
re = check_even_list([1,5,3])
print(re)

# Return all even numbers in a list
# Let's add more complexity, we now will return all the even numbers in a list, 
# otherwise return an empty list.

def check_even_list(num_list):
    # placeholder Variables
    even_numbers = []
    
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we append the even number
        if number % 2 == 0:
            even_numbers.append(number)
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return even_numbers
ev = check_even_list([1,2,3,4,5,6])
print(ev)


# Returning Tuples for Unpacking
# ** Recall we can loop through a list of tuples and "unpack" the values within them**

stock_prices = [('AAPL',200),('GOOG',300),('MSFT',400)]
for item in stock_prices:
    print(item)
for stock,price in stock_prices:
    print(stock)
for stock,price in stock_prices:
    print(price)

# Similarly, functions often return tuples, to easily return multiple results for later use.
# Let's imagine the following list:

work_hours = [('Abby',100),('Billy',400),('Cassie',800)]
# The employee of the month function will return both the name and number of hours worked for 
# the top performer (judged by number of hours worked).

def employee_check(work_hours):
    
    # Set some max value to intially beat, like zero hours
    current_max = 0
    # Set some empty value before the loop
    employee_of_month = ''
    
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    
    # Notice the indentation here
    return (employee_of_month,current_max)

wrk = employee_check(work_hours) #('Cassie', 800)
print(wrk)

# Interactions between functions
# Functions often use results from other functions, let's see a simple example through a guessing game. 
# There will be 3 positions in the list, one of which is an 'O', a function will shuffle the list, another 
# will take a player's guess, and finally another will check to see if it is correct. This is based on the 
# classic carnival game of guessing which cup a red ball is under.

example = [1,2,3,4,5]
from random import shuffle
# Note shuffle is in-place
shuffle(example)
print(example)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)
print(result)
