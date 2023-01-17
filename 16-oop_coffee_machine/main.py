from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


machine_state = True
# while machine_state == "on"
while machine_state:
    # ask customers to select from the list of coffee avaliable
    try:
        coffee = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()
    except KeyboardInterrupt:
        break

    # if user inputs 'off' turn off coffee machine and end program
    if coffee == "off":
        break
    # if user inputs 'report' print resources available
    if coffee == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # check if the customer selected coffee from the menu
        select_coffee = menu.find_drink(coffee)
        if select_coffee:
            # check if we have sufficient resources
            if coffee_maker.is_resource_sufficient(select_coffee):
                # verify transaction
                if money_machine.make_payment(select_coffee.cost):
                    # make coffee
                    coffee_maker.make_coffee(select_coffee)
