import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

clear = lambda: os.system('clear')

def yes_or_no(msg):
    players_choice = input(f"{msg}")
    if players_choice.lower() == 'y' :
        return True
    elif players_choice.lower() == 'n' :
        return False
    else:
        print("Invalid Option. Choose again.")
        return yes_or_no(msg)

def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2 : return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)

def print_score(player_hand, computer_hand):
    print(f"    Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
    print(f"    Computer's first card: {computer_hand[0]}")

def compare(player_score, computer_score):
    if player_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Lose, opponent has a Blackjack!"
    elif player_score == 0:
        return "Win with a Blackjack!"
    elif player_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose"

def play_game():
    is_game_over = False
    player_hand = []
    computer_hand = []

    print(logo)

    # Overture
    # one card for player, one card for computer, another card to player, another card to computer
    for _ in range(2):
        player_hand.append(deal_card())
        computer_hand.append(deal_card())

    while not is_game_over:

        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)

        print_score(player_hand, computer_hand)

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            player_wanna_deal = yes_or_no("Type 'y' to get another card or type 'n' to pass:")
            if player_wanna_deal: 
                player_hand.append(deal_card())
            else:
                is_game_over = True
    
    while computer_score < 17 and computer_score != 0:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand) 
    
    print(f"    Your final hand is {player_hand}, final score is {21 if player_score == 0 else player_score}")
    print(f"    Computer's final hand is {computer_hand}, final score is {21 if computer_score == 0 else computer_score}")
    print(compare(player_score, computer_score))

player_want_to_play = yes_or_no("Do you want to play a game of Blackjack? Type 'y' or 'n':")

while player_want_to_play:
    clear()
    play_game()
    player_want_to_play = yes_or_no("Do you want to play a game of Blackjack? Type 'y' or 'n':")