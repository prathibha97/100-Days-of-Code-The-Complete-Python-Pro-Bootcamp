from random import randint
from art import logo


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# function to check user's guess agains actual answer
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1

    else:
        print(f"You got it. The answer was {answer}")


# make functions to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)

    # choosing a random number between 1 and 100
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()
    guess = 0

    # repeat if they get it wrong
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # let the user guess a number
        guess = int(input("Make a guess: "))

        # track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again")


game()
