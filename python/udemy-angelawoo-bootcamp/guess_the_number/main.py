# imports
import random
import re
from art  import logo

#functions
def set_difficulty():
    '''
    return the number of attempts based on difficulty chosen
    '''
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5
    else:
        print("Sorry, Wrong Option. Choose again.")
    
    return set_difficulty()

def make_guess():
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = input("Make a guess: ")
    if validate_guess(guess) :
        return int(guess)

def validate_guess(guess):
    regex = re.compile(r"[0-9]+")
    match = regex.match(str(guess))

    if not match:
        print(f"'{guess} is not numeric! Type another valid guess:")
        make_guess()
    else :
        return True

def compass(guess):
    if guess - answer > 0 :
        print("Too High")
        return False
    elif guess - answer < 0 :
        print("Too Low")
        return False
    else:
        return True

# Global Variable
game_is_over = False

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 100)

attempts = int(set_difficulty())

while not game_is_over:

    while attempts > 0:
        guess = make_guess()
        if compass(guess) :
            break
        else:
            attempts -= 1
            if attempts > 0 :
                print("Guess again.")
    
    game_is_over = True

if attempts == 0 :
    print("You've run out of guesses, you lose.")
else:
    print(f"You got it! The answer was {answer}.")