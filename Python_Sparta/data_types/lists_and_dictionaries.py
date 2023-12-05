# Lists
# Indexing lists starts at 0

example_list = [1, True, "string"] # Single data types ideal
print(example_list[0])

shopping_list = ["eggs", "bread", "cheese"]
shopping_list[1] = "bananas" # This replaces index 1 with another string
print(shopping_list)

shopping_list.append("bacon") # adds an item
print(shopping_list)

shopping_list.pop() # removes the last entry added
print(shopping_list)

print(shopping_list.index("eggs")) # returns the index of the item in the list

# Dictionaries

# Key value pairs, identify key and the value for it with :
contact_list = {
    "Jane": "07867553366"
}

# When you print a dictionary, it will print the value for it
print(contact_list["Jane"])

contact_list["Bob"] = "07896473817"
print(contact_list["Bob"])

contact_alphabet = {
    "a": {
        "annabell": "0756432456"
    },
    "b": {
        "barbara": "0765897657"
    },
    "c": {
        "clint": "0746536271"
    }
}

print(contact_alphabet["c"]['clint'])

theList = []
theList.append(1234)
theList.append(4567)
theList.append(99)
theList.append(5)
print(theList)
print(len(theList))