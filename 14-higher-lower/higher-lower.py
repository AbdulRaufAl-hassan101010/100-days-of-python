import random
from data import data
import os
import arts


def is_correct(account_a, account_b, answer):
    "Take the accounts and compare if the account with the  highest account followers count == answer, return True if that is case and False for otherwise"
    if account_a > account_b:
        return answer == "a"
    elif account_a < account_b:
        return answer == "b"
    else:
        return False


def question(account):
    "Generate a question from selecting a random account from accounts"
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return (f"{account_name}, a {account_description} in {account_country}.")


def choose_account(first_account):
    "Generate second question and caompares if the first question doesn't have the same followers count, if it does it change question until both accounts have different followers count "
    second_account = random.choice(data)
    if first_account["follower_count"] == second_account["follower_count"]:
        choose_account(first_account)
    return second_account


def play_game():
    scores = 0
    # select first random account to compare
    account_a = random.choice(data)

    # if user haven't guessed a wrong answer keep playing
    continue_playing = True
    while continue_playing:
        # select second random account to compare
        account_b = choose_account(account_a)

        # print question
        print(arts.logo)
        print(f"Your score is:{scores}")
        print(f"Compare A: {question(account_a)}")
        print(arts.vs)
        print(f"Compare B: {question(account_b)}")

        # ask user which one is higher A or B
        try:
            answer = input("Who has the highest followers? 'A' or 'B' ").lower()
        except KeyboardInterrupt:
            return

        # check if answer is correct, if is correct +1 to scores else end game
        if is_correct(account_a["follower_count"], account_b["follower_count"], answer):
            scores += 1
            # set account a to account b
            account_a = account_b
            # clear terminal
            os.system("cls")
        else:
            print(f"Game has eneded you scored:{scores}")
            continue_playing = False


# start game
play_game()
