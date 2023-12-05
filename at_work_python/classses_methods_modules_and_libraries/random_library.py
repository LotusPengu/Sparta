import random
import math     # if you want to learn more about a module/library, then read the official documentation
import os
import requests

""" random module and math module """
print(random.randint(1,6))

float_num = 35.9236

print(math.floor(float_num))    # ceiling and floor (rounding up and down)
print(math.ceil(float_num))

""" os module checking working directory """
working_directory = os.getcwd()
print(working_directory)

""" requests install from pip, checking various details from bbc website """
request_bbc = requests.get("https://www.bbc.co.uk")

print(request_bbc)
print(type(request_bbc))
print(request_bbc.status_code)
print(request_bbc.content)