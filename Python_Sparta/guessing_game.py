import random

# Number guessing game

"""
1. Random number in a range
2. Capture guess
3. Evaluate user guess
"""

game_random_number = random.randint(1, 100)

game_active = True

while game_active:
    game_start_message = "guess a number between 1 - 100"
    user_guess = int(input())
    if user_guess == game_random_number:
        print("you guessed correct")
        game_active = False
    elif user_guess < game_random_number:
        print("Too low, guess again")
    else:
        print("Too high, guess again")
