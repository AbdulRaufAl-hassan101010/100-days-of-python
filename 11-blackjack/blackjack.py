import random
import os


def deal_cards():
    """
        add cards to each player from cards
    """
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
    return random.choice(cards)


def calculate_scores(cards):
    """
        calculate scores,
        return 
            0 if score == 21,
            -1 if score > 21,  
            score     
    """
    score = sum(cards)
    if score == 21:
        return 0

    # 11 is included in cards and score > 21, replace 11 with 1
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)

    if score > 21:
        return -1

    return score


def results(dealer_score, player_score):
    """
        diplay winner 
    """
    if player_score < 0:
        return "Dealer Won"
    if dealer_score == player_score:
        return "Draw"
    if player_score == 0 or player_score > dealer_score:
        return "You won!!"

    return "Dealer Won"


def play_game():
    player_cards = []
    dealer_cards = []
    end_game = False

    # display logo
    from arts import logo
    print(logo)

    # give each player 2 card just show dealers first card
    for _ in range(2):
        player_cards.append(deal_cards())
        dealer_cards.append(deal_cards())

    player_score = calculate_scores(player_cards)
    dealer_score = calculate_scores(dealer_cards)
    while not end_game:

        # check players scores
        player_score = calculate_scores(player_cards)
        dealer_score = calculate_scores(dealer_cards)

        # display player cards and just the display the dealer's first card
        print(
            f"Your Cards: {player_cards}, your current score: {sum(player_cards)}")
        print(f"Dealer's Card: {dealer_cards[0]}")

        # check if player has won or exceed 21
        if player_score <= 0:
            end_game = True
            break

        # ask player if play wants to continue playing
        continue_playing = input(
            "Do you want another card? type 'y' or 'n' ").lower()

        if continue_playing == 'n':
            end_game = True
            break

        # add card to player as requested
        player_cards.append(deal_cards())

        os.system('cls')

    # add cards to dealer if dealers score < 17
    while dealer_score < 17 and dealer_score > 0:
        dealer_cards.append(deal_cards())
        dealer_score = calculate_scores(dealer_cards)

    # display results
    os.system('cls')
    print(f"Your Cards: {player_cards}, Dealer score: {sum(player_cards)}")
    print(f"Dealer Cards: {dealer_cards}, Dealer score: {sum(dealer_cards)}")
    print(results(dealer_score, player_score))

    # ask player if player wants to play again
    play_again = input("Do you want to play again? 'y' or 'no' ")

    if play_again == 'y':
        play_game()


# start game
play_game()
