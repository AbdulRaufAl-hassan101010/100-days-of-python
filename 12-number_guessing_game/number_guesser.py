from random import randint
import sys
import os
from arts import logo

HARD_LEVEL_LIVES = 5
EASY_LEVEL_LIVES = 10


def set_difficulty():
    # ask user which level the user wants play "easy" or "hard"
    try:
        level = input("Do you want to play 'hard' or 'easy'? ").lower()
    except KeyboardInterrupt:
        return

    if level == "hard":
        return HARD_LEVEL_LIVES
    else:
        return EASY_LEVEL_LIVES


def check_answer(answer, guess, lives):
    # if user's guess is answer end loop(end game)
    if guess == answer:
        print(f"You guessed the correct answer:{answer}")
        return lives
    if answer > guess:
        print(f"Too Low")
        return lives - 1
    if answer < guess:
        print(f"Too High")
        return lives - 1

    if lives < 1:
        print(f"You have no lives left the answer is {answer}")


def start_game():
    # display logo
    print(logo)

    # generate random number
    answer = randint(1, 100)

    # set game difficulty base on user input 'hard'=5lives and 'easy'=10lives
    lives = set_difficulty()

    # while user lives > 0 or user's guess not answer
    users_guess = 0
    while lives > 0 and users_guess != answer:
        # display lives
        print(f"You have {lives} left.")

        # ask user to guess a number between 1 - 100
        try:
            users_guess = int(input("Guess a number between 1 - 100? "))
        except TypeError:
            sys.exit("Guess must be an integer")
        except KeyboardInterrupt:
            sys.exit()

        # check if user's guess the correct answer
        lives = check_answer(answer, users_guess, lives)

    # ask user if user wants to play again ?
    try:
        play_again = input(
            "Do you want to play again? 'y' or 'no' ").lower()
    except KeyboardInterrupt:
        return
    # if user want to play again restart game
    if play_again == 'y':
        os.system("cls")
        start_game()


start_game()
