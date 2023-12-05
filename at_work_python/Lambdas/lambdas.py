def add(num1, num2):
    return num1 + num2

print(add(2, 2))

addition = lambda num1, num2: num1 + num2       # have defined the parameters and what we want them to do

print(addition(2, 2))

savings = [234.00, 555.00, 672.00, 78.00]

bonus = list(map(lambda x: x * 1.1, savings))

print(bonus)

""" lambdas allow you to create simple anonymous functions that can  """
