# if x:
#     if y:
#         code-statement
# else:
#     another-code-statement
# Note how Python is so heavily driven by code indentation and whitespace. This means that code readability is a core part of the design of the Python language.
# CONTROL FLOW
# To control this flow of logic we use some keywords:
# if elif and else
x = False
if x:
    print('x was True!')
else:
    print('I will be printed in any case where x is not true')

# Multiple Branches
# Let's get a fuller picture of how far if, elif, and else can take us!

# We write this out in a nested structure. Take note of how the if, elif, and else line up in the code. This can help you see what if is related to what elif or else statements.

# We'll reintroduce a comparison syntax for Python.

loc = 'Bank'

if loc == 'Auto Shop':
    print('Welcome to the Auto Shop!')
elif loc == 'Bank':
    print('Welcome to the bank!')
else:
    print('Where are you?')

car = 'Black'

if car == 'Red':
    print('The Car is red')
elif car == 'Black':
    print("You're Correct")
else:
    print('Guess the color')