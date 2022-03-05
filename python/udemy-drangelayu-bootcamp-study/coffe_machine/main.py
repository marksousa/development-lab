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

    if client_choice in MENU.keys(): return selling_flow({client_choice: MENU.get(client_choice)})
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
    for eachResource in resources.keys():
        print(f"{ eachResource.capitalize() }: {resources.get(eachResource)}")

def get_till_amount():
    return print(f"Money: {till_amount.get('money')}")

def verify_disponibility(drink):
    resource = MENU.get(drink)
    return check_resources(resource["ingredients"])

def check_resources(ingredients):
    for resource in resources:
        if resources[resource] < ingredients[resource] : return False
    return True 

def process_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    client_amount_coin = quarters * coins_accepted["quarters"] + dimes * coins_accepted["dimes"] + nickles * coins_accepted["nickles"] + pennies * coins_accepted["pennies"]
    return client_amount_coin

def selling_flow(valid_client_choice):
    print(valid_client_choice.keys())
    
    # 1. Check the resources to confirm if drink is available
    # # 2. Customer insert the coins
    # # 3. Check the transaction($)
    #     # 3.1. If >=, calculate the change, deduct the ingredients from the resources inventory and prepare the drink,
    #     # 3.2. If No, "Print "Sorry that's not enough money. Money refunded."
    # if valid_client_choice :
    #     client_wallet = process_coins()
    #     if client_wallet >= int(valid_client_choice["cost"]):
    #         print("Ok.")
    #     else :
    #         print("Not enough.")

def deduct_resources(drink):
    resources = MENU.get(drink)
    ingredients = resources["ingredients"]

# def prepare_drink(drink):
#     print(MENU.get(drink))

while machine_on:
    client_input()