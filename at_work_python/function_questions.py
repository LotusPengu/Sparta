print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1
def divisors(number: int) -> list:
    divisors_list = []
    for i in range(1, number + 1):       # have to + 1, as range goes up to, but not including, the second parameter
        if number % i == 0:
            divisors_list.append(i)      # adds any number that can be cleanly divided into the given number
    return divisors_list

print(divisors(26))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1
""" can label function names in more detail if so desire """
def is_factor(num1: int, num2: int) -> bool:
    if num2 in divisors(num1) or num1 in divisors(num2):
        return True
    else:
        return False

print(is_factor(9,8))

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A1
def alphabet_position(letter: str) -> int:
    return alphabet.index(letter.lower()) + 1

print(alphabet_position("D"))

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A1

def id_generator(name_string: str) -> str:
    id = ""
    for letter in name_string:
        id += str(alphabet_position((letter)))
    return id

print(id_generator("bob"))

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

def password_generator(name_string: str) -> str:
    password_number = 0
    for i in id_generator(name_string):
        password_number += int(i)
    return str(int(id_generator(name_string)) - password_number)

print(password_generator("bob"))

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A1
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

# A2

def is_prime(number:int) -> bool:
    prime = True
    for i in range(2, int(number)):
        if int(number) % i == 0:
            prime = False
    return prime

print(is_prime(111))

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

