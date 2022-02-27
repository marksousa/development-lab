# imports
from art import logo
from art import vs

import game_data
import random
import os

clear = lambda: os.system('clear')

#TODO#1: import the logo game
# First Mode (if art.py is small, ok use this. It imports all art.py file)
# import art 
# print(art.logo)
# Second Mode
# Above is a good choice if you wanna just one variable(logo) from art.py
# all imports are in the begging.

#TODO#2: Create a function that sort two different dictionary elements from list data in game_data.py
def sort_data(el = {}):
    """Sort two differents dictionary elements from list data in game_data.py."""
    element_sorted = random.choice(game_data.data)
    if element_sorted != el: return element_sorted 
    # print("duplicated.. sorting again")
    return sort_data(el)


#TODO#3: Create a Function that take two differents elements from game data
def load_comparison():
    """Takes two differents elements from game data and return the element which has the higher followers count."""
    A = sort_data()
    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}")
    print(vs)
    B = sort_data(A)
    print(f"Compare B: {B['name']}, {B['description']}, from {B['country']}")
    return higher_follower_count(A, B)

#TODO#4: Create a Function that inputs a valid guess's player
def player_input(msg):
    """ Display an input and validate the players choice."""
    players_choice = input(msg)
    if players_choice.lower() == 'a' : return "A"
    if players_choice.lower() == 'b' : return "B"
    print("Invalid Option. Choose again.")
    return player_input(msg)

#TODO#5: - Create a function to make the comparison and return the element which has the higher follower count
def higher_follower_count(A, B):
    """ Compares follower count key beetwen two dictionaries"""
    if A['follower_count'] >= B['follower_count']: return "A"
    return "B"

def clear_console():
    """ Clear the Console and Prints the Logo"""
    clear()
    print(logo)

#TODO#6: Create a function that organizes the game flow
def start_game():
    score = 0
    is_game_over = False
    print(logo)

    while not is_game_over:
        answer = load_comparison()
        player_guess = player_input("Who has more followers? Type 'A' or 'B': ")
        if player_guess == answer :
            score += 1
            clear_console()
            print(f"You're right! Current score: {score}.")
        else :
            is_game_over = True
            clear_console()
            print(f"Sorry, that's wrong. Final score: {score}")

start_game()