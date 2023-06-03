# while Loops
# The while statement in Python is one of most general ways to perform iteration. A while statement will 
# repeatedly execute a single statement or group of statements as long as the condition is true.
# The reason it is called a 'loop' is because the code statements are looped through over and over again 
# until the condition is no longer met.

# The general format of a while loop is:

# while test:
#     code statements
# else:
#     final code statements

# Let’s look at a few simple while loops in action.

x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1

###############
x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    
else:
    print('All Done!')

###############
x = 0
while x < 10:
    print(x)
    x+=1
    if  x == 3:
        print('wow')
    else:
        print('continue')

   ############

x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('Breaking because x==3')
        break
    else:
        print('continuing...')
        continue