# String concatenation and escape characters

first_name = "jane"
last_name = "doe"
full_name = first_name + ' ' + last_name
age = 25

# Age has to be converted to a string in order for concatenation to work - known as Casting
print(full_name + ' ' + str(age))

# Escape characters allow the code to ignore a character, e.g., another set of quotes in a string
text = "someone then said, \"text can be tricky\""
print(text)
