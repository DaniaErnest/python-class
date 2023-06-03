# Formatting with the .format() Method

# This make the INSTERTED to be part of the Sentence
print('This string is {}'.format('INSERTED'))

# This set the Order in which dey are in the sentence
print('The {2} {1} {0}'.format('fox','brown','quick'))

# Assigning it to a variable and passing it
print('The {c} {b} {a}'.format(a='fox',b='brown',c='quick'))

# float Formatting "{value:width.precision f}"
result = 100/777
print(result)
print("The result was {r:1.4f}".format(r=result))


# f string format
name = "jose"
age = 42
print(f"Hello, my name is {name}, i am {age}")

# Formatting with placeholders
# You can use %s to inject strings into your print statements.
#  The modulo % is referred to as a "string formatting operator".
print("I'm going to inject %s here." %'something')
print("I'm going to inject %s text here, and %s text here." %('some','more'))
x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here."%(x,y))