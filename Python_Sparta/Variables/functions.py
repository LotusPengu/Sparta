# Functions

# DRY Don't Repeat Yourself

"""
def print_item(first_name, last_name):
    print(first_name + ' ' + last_name)

print_item("bob","bobbills") # Calls the function, as long as all parameters are filled
"""

def full_name(first_name,last_name):
    return first_name + ' ' + last_name

def print_name(data_type):
    print(data_type)

print_name((full_name("jane","doe")))

