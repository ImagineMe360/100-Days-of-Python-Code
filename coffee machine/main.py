from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

os.system('cls' if os.name == 'nt' else 'clear')

menu = Menu()
# menu_item = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# print(menu.find_drink('latte'))

is_off = False

while not is_off:
    choice = input(f"What would you like? ({menu.get_items()}): ")

    if choice.lower() == 'e':
        choice = 'espresso'
    if choice.lower() == 'l':
        choice = 'latte'
    if choice.lower() == 'c':
        choice = 'cappuccino'

    if choice.lower() == 'latte' or choice.lower() == 'espresso' or choice.lower() == 'cappuccino':
        drink = menu.find_drink(choice)
        has_enough_resources = coffee_maker.is_resource_sufficient(drink)
        if has_enough_resources:
            has_enough_money = money_machine.make_payment(drink.cost)
            if has_enough_money:
                coffee_maker.make_coffee(drink)
    elif choice == 'r':
        coffee_maker.report()
        money_machine.report()
    else:
        is_off = True