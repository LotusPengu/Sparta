# Indentation is important in Python, it is how it sees which code is blocked with what

if 2 == 2:
    print("These numbers are equal")


"""
Cinema system age management
1. If someone is under 12 - U, PG, and  12 films are available
2. If someone is under 15 - U, PG, 12, and 15 films are available
3. Over 18 - all films are available
"""

customer_age = 15

if customer_age <= 12:
    print("U, PG, and 12 films are available")
elif customer_age <= 15:
    print("U, PG, 12, and 15 films are available")
else:
    print("all films are available")


"""
Chatbot greetings
1. Between 05:00 - 12:00 - Good morning 
2. Between 12:00 - 18:00 - Good afternoon
3. Between 12:00 - 18:00 - Good evening 
"""

time_of_day = 6

# Or & And

if time_of_day > 5 and time_of_day < 12:
    print("Good Morning")
if time_of_day > 12 and time_of_day < 18:
    print("Good Afternoon")
else:
    print('Good Evening')


