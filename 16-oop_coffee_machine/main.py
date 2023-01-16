from coffee_maker import CoffeeMaker

coffeeMaker = CoffeeMaker()

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
