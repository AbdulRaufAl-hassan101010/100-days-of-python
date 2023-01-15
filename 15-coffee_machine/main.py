from data import MENU
from data import resources


def display_resources():
    """Output the resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def coins_calculator():
    """return summation of coins"""
    pennies = float(input("How many pennies? "))
    nickles = float(input("How many nickles? "))
    dimes = float(input("How many dimes? "))
    quarters = float(input("How many quarters? "))

    return (pennies * 0.01) + (nickles * 0.05) + (dimes * 0.10) + (quarters * 0.25)


def is_resource_sufficient(coffee, ingredients):
    """check if resources are sufficent"""
    # check if machine has enough quantity to make coffee
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(
                f"Machine doesn't have enough {ingredient} to make {coffee}")
            print(f"Your ${coins} has been refunded")
            return False
    return True


def make_coffee(coffee):
    """Make coffee"""
    ingredients = MENU[coffee]["ingredients"]
    # check if machine has enough quantity to make coffee
    if (is_resource_sufficient(coffee, ingredients)):
        # make coffee, use resources
        for ingredient in ingredients:
            resources[ingredient] -= ingredients[ingredient]
        print(f"Here is your {coffee}. Enjoy")
        return True
    return False


def customer_change(coins):
    """return customer change coins - cost"""
    # if coins > coffee price
    change = coins
    cost = MENU[coffee]["cost"]
    if coins > cost:
        change = coins - cost
        print(f"Here is your change {change}")
    return change


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
        display_resources()
    else:
        # if user select a coffee
        if coffee != "espresso" and coffee != "latte" and coffee != "cappuccino":
            print(
                f"{coffee} is not available. Please Select coffee from our list (espresso/latte/cappuccino)")
        else:
            # ask customer to insert coins
            print("Please insert coins.")
            coins = coins_calculator()

            # verify transaction if coins < coffee price
            if coins < MENU[coffee]["cost"]:
                # refund customer
                print(
                    f"Sorry, you dont have enough coins to purchase {coffee}")
                print(f"Your ${coins} has been refunded")
            else:
                # else make coffee
                if make_coffee(coffee):
                    # give customer change
                    customer_change(coins)

                    # add money to sales
                    cost = MENU[coffee]["cost"]
                    resources["money"] += cost
