print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1
print(x[0:5])

# A2 with a for loop

counter = 1
for number in x:
    if counter <= 5:
        print(number)
        counter += 1

# A3 with range

# A1
for i in range(5):
    print(x[i])

print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)

# A1
for num in x:
    if num % 2 == 0:
        print(num, end=" ")  # end adds a string to the output of the prior print

print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)

# A1
for num2 in x[0:5]:
    if num2 % 2 == 0:
        print(num2, end=" ")

# A2 using counters
counter = 1
for number in x:
    if counter > 5:
        break
    elif number % 2 == 0:
        print(number)
    counter += 1

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A1
list = []
for name in names: # Want to look at each name so 'for' loop is appropriate
    list.append(name[0]) # Adds the first letter of each name to the empty list
print(list)

print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

""" Let's just ignore this monstrosity
list2 = []
list2.append(names[0].index(" "))
list2.append(names[1].index(" "))
list2.append(names[2].index(" "))
list2.append(names[3].index(" "))
list2.append(names[4].index(" "))
print(list2)
"""

space_index = []
for name in names:
    space_index.append(name.index(" "))
print(space_index)

print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A1
initials = []
for name in names:
    separate = name.split()
    initials.append(separate[0][0] + separate[-1][0])
print(initials)

# A2
initials_2 = []
for name in names:
    initials_2.append(name[0] + name[name.index("") + 1])
print(initials_2)

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "Bye", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]

""" no 
list_to_tuple = tuple(list_of_lists[0]) + tuple(list_of_lists[1]) + tuple(list_of_lists[2]) + tuple(list_of_lists[3])
tuple_to_set = set(list_to_tuple)
print(tuple_to_set) """

lst = []
for item in list_of_lists:
    lst.append(set(item))
print(lst)

no_duplicates = []
for item in list_of_lists:
    if len(set(item)) == len(item):
        no_duplicates.append(item)
print(no_duplicates)

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

program_active = True
while program_active:
    num_given = input("Enter a number greater than 100:")
    if float(num_given) > 100.0:
        print(num_given, "is over 100")
        program_active = False
    else:
        print(num_given, "is not over 100, try again")

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

prime = True
for i in range(2, int(num_given)):
    if int(num_given) % i == 0:
        prime = False
        print(num_given, "is a prime number")
    else:
        print(num_given, "is not a prime number")





"""
def prime_number():
    program_active = True
    while program_active:
        num_given = int(input("Enter a number"))
        if num_given == 1:
            print(num, "is not a prime number")
        elif num_given > 1:
            for i in range(2, num_given):
                if (num_given % i) == 0:
                    print(num_given, "is not a prime number")
                    print(i, "times", num_given, "is", num_given)
                    break
            else:
                print(num_given, "is a prime number")

prime_number()
"""

