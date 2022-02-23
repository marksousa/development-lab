#Python Notes

################### Scope ####################

enemies = 1

def increase_enemies():
enemies = 2
print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# #Local Scope

# def drink_potion():

# potion_strength = 2

# print(potion_strength)

# drink_potion()

#Global scope
player_health = 10

def game():
def drink_potion():
potion_strength = 2
print(potion_strength)
drink_potion()

print(player_health)

# #There is no Block Scope

Remember that in Python there is no block scope. Inside a if/else/for/while code block is the same as outside it.

# if 3 > 2:

# a_variable = 10 # here we have global scope.. inside a if

game_level = 3
def create_enemie():
enemies = ['Skeleton', 'Zombie', 'Alien']
if game_level < 5 :
new_enemy = enemies[0] # "new_enemy" is inside a if but has scope inside create_enemie function. No Block Scope.

print(new_enemy)

#Modifying Global Scopes
enemies = 1

def increase_enemies():
print(f"Enemies inside the function {enemies}")
return enemies + 1

enemies = increase_enemies()
print(f"Enemies outside the function {enemies}")

#Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@iammarksousa"
