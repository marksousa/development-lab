from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker_object = CoffeeMaker()
menu_object = Menu()
money_machine_object = MoneyMachine()

machine_is_on = True


def generate_resources_report():
    """ Call the resources report. """
    coffee_maker_object.report()
    money_machine_object.report()


def turn_off():
    """ Turn off the coffee machine. Exit the program """
    quit()


def machine_available():
    """ Display an input, validate the client choice and returns the corresponding choice. """
    client_choice = input(f"What would you like? ({menu_object.get_items()}):").lower()

    if client_choice in menu_object.get_items():
        menu_item = menu_object.find_drink(client_choice)
        if coffee_maker_object.is_resource_sufficient(menu_item):
            if money_machine_object.make_payment(menu_item.cost):
                coffee_maker_object.make_coffee(menu_item)
    elif client_choice == 'report':
        generate_resources_report()
    elif client_choice == 'off':
        turn_off()
    else:
        print("Invalid Option. Try again.")
    return machine_available()


machine_available()

