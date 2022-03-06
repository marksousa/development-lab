from data import MENU
from data import resources
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

machine_on = True

coins_accepted = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

till_amount = {
    "money": 0
}

def client_input(msg = "What would you like? (espresso/latte/cappuccino):"):
    """ Display an input, validate the players choice and returns the corresponding choice. """

    client_choice = input(msg).lower()

    if client_choice in MENU.keys(): return selling_flow(client_choice)
    if client_choice == 'report': return generate_resources_report()
    if client_choice == 'off': return turn_off()
    print("Invalid Option. Try again.")
    return client_input()

def turn_off():
    machine_on = False
    quit()

def generate_resources_report():
    get_resources_inventory()
    get_till_amount()

def get_resources_inventory():
    for eachResource in resources:
        print(f"{ eachResource.capitalize() }: {resources.get(eachResource)}{ 'ml' if eachResource in ('water', 'milk') else 'g'}")

def get_till_amount():
    return print(f"Money: ${till_amount.get('money')}")

def drink_is_available(drink):
    resource = MENU.get(drink)
    return check_resources(resource["ingredients"])

def check_resources(ingredients):
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient] : return {'status': False, 'resource': ingredient}
    return {'status': True}  

def process_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    client_amount_coin = quarters * coins_accepted["quarters"] + dimes * coins_accepted["dimes"] + nickles * coins_accepted["nickles"] + pennies * coins_accepted["pennies"]
    return client_amount_coin

def deduct_resources(ingredients):
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]

def process_transation(client_pays, drink):
    dict_drink = MENU.get(drink)
    drink_price = dict_drink["cost"]
    if client_pays >= drink_price:
        till_amount["money"] += drink_price
        deduct_resources(dict_drink["ingredients"])
        change = client_pays - drink_price
        print(f"Here is ${change} dollars in change.")
        print(f"Here is your {drink}. ☕ Enjoy!")

    else: 
        print("Sorry that's not enough money. Money refunded.")

def selling_flow(client_drink_choice):
    available = drink_is_available(client_drink_choice)
    
    if available["status"]:
        client_pays = process_coins()
        process_transation(client_pays, client_drink_choice)
    else:
        not_enough = drink_is_available(client_drink_choice)
        print(f"Sorry, there is not enough {not_enough['resource']}.")

# Machine Main Function
while machine_on:
    client_input()