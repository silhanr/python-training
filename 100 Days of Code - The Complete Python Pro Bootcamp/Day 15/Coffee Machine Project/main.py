MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# resources = {
#     "water": 300,
#     "milk": 500,
#     "coffee": 1,
# }
def print_report():
    try:
        print(f'---- REPORT ----\nWater: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: ${resources["money"]}\n----------------')
    except KeyError:
        resources["money"] = 0
        print(f'---- REPORT ----\nWater: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: ${resources["money"]}\n----------------')


def check_resources(choice):
    # print(choice["ingredients"].keys())
    if choice["ingredients"]["water"] <= resources["water"]:
        if choice["ingredients"]["coffee"] <= resources["coffee"]:
            if "milk" in choice["ingredients"].keys():
                if choice["ingredients"]["milk"] <= resources["milk"]:
                    return True
                else:
                    print("Sorry there is not enough milk.")
                    return False
            else:
                return True
        else:
            print("Sorry there is not enough coffee.")
            return False
    else:
        print("Sorry there is not enough water.")
        return False

def deduct_resources(choice):
    resources["water"] -= choice["ingredients"]["water"]
    resources["coffee"] -= choice["ingredients"]["coffee"]
    if "milk" in choice["ingredients"].keys():
        resources["milk"] -= choice["ingredients"]["milk"]



def process_coins():

    print("\n---- Insert coins ----\n")
    try:
        quarters = int(input("Quarters: "))
        dimes = int(input("Dimes: "))
        nickles = int(input("Nickles: "))
        pennies = int(input("Pennies: "))

        return round(0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies, 2)
    except:
        print("Incorrect input!")
        return 0

def check_transaction(choice,money):

    if money >= choice["cost"]:
        change = round(money - choice["cost"],2)
        resources["money"] += choice["cost"]

        print(f"Your change is: ${change}")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO MAKE coffee

def machine():
    resources["money"] = 0
    run = True
    choice = ""
    while run:
        # Get user's input from prompt
        user_input = input('What would you like? (espresso/latte/cappuccino): ').lower()
        if user_input == "off":
            run = False
        elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            choice = MENU[user_input]

            if check_resources(choice):
                if check_transaction(choice,process_coins()):
                    deduct_resources(choice)
                    print(f"Here is your {user_input}. Enjoy")

        elif user_input == "report":
            print_report()
        else:
            print("Invalid input!!!!")





machine()