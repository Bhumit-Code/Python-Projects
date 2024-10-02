
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances of the classes


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


while True:

    get_items = menu.get_items()
    Type = input(f"Which type of coffee do you want? {get_items}")

    if Type == "report":
        coffee_maker.report()
        money_machine.report()
    elif Type == "off":
        break
    else:
        # Find the drink the user selected
        find_drink = menu.find_drink(order_name=Type)

        # Check if resources are sufficient
        if coffee_maker.is_resource_sufficient(find_drink):
            # Process payment
            if money_machine.make_payment(find_drink.cost):
                # Make the coffee
                coffee_maker.make_coffee(find_drink)
