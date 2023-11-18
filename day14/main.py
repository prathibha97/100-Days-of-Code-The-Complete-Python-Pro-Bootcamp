import os
import random
from art import logo, vs
from game_data import data


def format_data(account):
    """format the account data and return a printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess, a_followers, B_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > B_followers:
        return guess == "a"
    else:
        return guess == "b"


# display art
print(logo)

score = 0
game_should_continue = True
account_b = random.choice(data)


# make the game repeatable
while game_should_continue:
    # generate a random account from the game data

    # makeing accounts at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_a = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    # ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check if the user is correct
    ##  get follower counr of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # clear the screen
    os.system('clear')
    print(logo)

    # give user feedback on their guess
    if is_correct:
        # score keeping
        score += 1
        print(f"You're correct! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's not correct. Final score: {score}")
