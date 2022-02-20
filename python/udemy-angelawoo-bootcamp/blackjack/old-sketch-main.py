import random

blackjack = 21
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# sort card
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

def add_card(hand):
    # list1.extend(list2) add elements from list in return of sort_card()
    hand.extend(sort_card())
    return hand

# calculate hand's score
def hand_score(hand):
    score = 0
    for card in hand:
        score += card
    return score

def validation_input(msg):
    players_choice = input(f"{msg}")
    if players_choice.lower() == 'y' :
        return True
    elif players_choice.lower() == 'n' :
        return False
    else:
        print("Invalid Option. Choose again.")
        return validation_input(msg)

def went_over(hand):
    if hand_score(hand)-blackjack > 0:
        return True
    else:
        return False

def players_turn(player_hand, computer_hand):
    print(f"    Your cards: {player_hand}, current score: {hand_score(player_hand)}")
    print(f"    Computer's first card: {computer_hand[0]}")

def verify_winner(player_final_score, computer_final_score):
    if abs(blackjack-player_final_score) < abs(blackjack - computer_final_score):
        print("You Win")
    elif abs(blackjack-player_final_score) == abs(blackjack - computer_final_score):
        print("Draw")
    else: 
        print("You Lose")

player_want_to_play = validation_input("Do you want to play a game of Blackjack? Type 'y' or 'n':")

while player_want_to_play:
    player_hand = sort_card()
    computer_hand = sort_card()
    player_hand = sort_card()

    players_turn(player_hand, computer_hand)

    player_wants_more_card = validation_input("Type 'y' to get another card, type 'n' to pass: ")

    while player_wants_more_card:
        add_card(player_hand)
            
    if player_hand["status"] == 'went-over':
        print(f"    Your final hand: {player_hand}, final score: {hand_score(player_hand)}")
        print("You went over. You lose.")
        break
    elif player_hand[-1]["status"] == 'blackjack':
        print(f"    Your final hand: {player_hand}, final score: {hand_score(player_hand)}")
        
    else:
        print(f"    Your final hand: {player_hand}, final score: {hand_score(player_hand)}")
        player_final_score = hand_score(player_hand)

        while hand_score(computer_hand) <= 17:
            add_card(player_hand)
            
        print(f"    Computer's final hand: {computer_hand}, final score: {hand_score(computer_hand)}")
    
        if computer_hand[-1]["status"] == 'went-over':
            print("Opponent went over. You win 😁")
        else:
            computer_final_score = hand_score(computer_hand)

            verify_winner(player_final_score, computer_final_score)