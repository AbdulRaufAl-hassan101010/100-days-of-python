from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu

coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
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
        coffeeMaker.report()
        moneyMachine.report()
    else:
        # if user select a coffee
        if menu.find_drink(coffee) == None:
            print(
                f"{coffee} is not available. Please Select coffee from our list (espresso/latte/cappuccino)")
        else:
            # ask customer to insert coins
            print("Please insert coins.")

            # verify transaction 
            select_coffee = menu.find_drink(coffee)
            if moneyMachine.make_payment(select_coffee.cost):
                # make coffee
                if coffeeMaker.is_resource_sufficient(select_coffee):
                    coffeeMaker.make_coffee(select_coffee)
