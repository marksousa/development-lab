import random

def yes_or_no(msg):
    players_choice = input(f"{msg}")
    if players_choice.lower() == 'y' :
        return True
    elif players_choice.lower() == 'n' :
        return False
    else:
        print("Invalid Option. Choose again.")
        return yes_or_no(msg)

def sort_card(qtd = 1):
    counter = 0
    hand = []
    while(counter < qtd):
        sort = random.choice(cards)
        if sort == 11 and sort + hand_score(hand) > 21:
            sort = 1
        hand.append(sort)
        counter += 1
    return hand

player_want_to_play = yes_or_no("Do you want to play a game of Blackjack? Type 'y' or 'n':")

while player_want_to_play:
    #Overture
    #player gets one card
    player_hand = sort_card()

    #computer gets onde card
    computer_hand = sort_card()

    #player gets another card
    player_hand = sort_card()



    # Remeber to make a false condition
    player_want_to_play = False