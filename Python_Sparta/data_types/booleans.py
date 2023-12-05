"""
Booleans and equality operators

  Operator |        Meaning
    ==     |  equal to
    !=     |  not equal to
    >      |  greater than
    <      |  less than
    >=     |  greater than or equal to
    <=     |  less than or equal to
"""

# True or false

print(type(True))
print(4 == 4)
print(2 == 4)
print(2 != 4)

"""
You cannot compare a integer to a string, 
unless the value of the string is accompanied by a function that causes it to give an int e.g., len()
"""

print(2>len("hello"))
print(bool(0)) # Anything other than 0 is true