#indexing and Slicing with String
mystring = "ABCDEFGHIJ"
print(mystring[2])
print(mystring[2:]) #start from 2
print(mystring[:4]) # don't get to 4
print(mystring[1:5]) # start from 1, don't get to 5
print(mystring[::2]) # ACEGI: this mean step size i.e use step size 2
print(mystring[2:5:2]) # CE: start from 2, don't get to 5, use step size 2
print(mystring[::-1])# This reverse a String

#concantination
na = "Tosin"
delna = na[1:]
print(delna)
sln = "f" + delna # concant "+"
print(sln)