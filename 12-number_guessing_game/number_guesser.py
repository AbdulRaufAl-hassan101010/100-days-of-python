from random import randint
import sys
import os


from arts import logo


def start_game():
    # display logo
    print(logo)

    # generate random number
    answer = randint(1, 100)

    # ask user which level the user wants play "easy" or "hard"
    try:
        level = input("Do you want to play 'hard' or 'easy'? ").lower()
    except KeyboardInterrupt:
        return

    # if easy user has 10 lives
    lives = 10
    # else if user chose hard, give user 5 lives
    if level == 'hard':
        lives = 5

    # while user lives > 0 or user's guess not answer
    users_guess = True
    while lives > 0 and users_guess != answer:
        # ask user to guess a number between 1 - 100
        try:
            users_guess = int(input("Guess a number between 1 - 100? "))
        except TypeError:
            sys.exit("Guess must be an integer")
        except KeyboardInterrupt:
            sys.exit()

        # if user's guess is answer end loop(end game)
        if users_guess == answer:
            break

        # if  answer > user's guess print message telling the user
        if answer > users_guess:
            print(f"Your answer > {users_guess}")

        # if user's guess < answer print message telling the user
        if answer < users_guess:
            print(f"Your answer < {users_guess}")

        # take one user live
        lives -= 1
        print(f"You have {lives} left.")
        # repeat until user's live < 1 or user's guess == answer

    # if user is out of lives end game
    if lives < 1:
        print("Game Over!!")
    else:
        # user got the anwser
        print("You won!!")
    print(f"The number is {answer}")

    # ask user if user whants to play again ?
    # ask user which level the user wants play "easy" or "hard"
    try:
        level = play_again = input(
            "Do you want to play again? 'y' or 'no' ").lower()
    except KeyboardInterrupt:
        return
    # if user want to play again restart game
    if play_again == 'y':
        os.system("cls")
        start_game()


start_game()
