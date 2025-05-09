coffee_menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18
        },
        "cost": 1.50
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.50
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.00
    }
}
# give coffee machine, certain resources that it uses up per coffee made
resources = {
    "water": 500,
    "milk": 250,
    "coffee": 150,
    "money": 0
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}
# in first function make a hidden report option that gives current status of whats inside
def report():
        for items in resources:
            print(items, resources[items])



def payment(coins, command_console):
    amount1 = int(input("How many quarters will you insert?")) * coins["quarters"]
    amount2 = int(input("How many dimes will you insert?")) * coins["dimes"]
    amount3 = int(input("How many nickels will you insert?")) * coins["nickels"]
    amount4 = int(input("How many pennies will you insert?")) * coins["pennies"]

    total = amount1 + amount2 + amount3 + amount4
    # when user asks for coffee and resources are met ask for coins
    # make function that asks for amount of pennies, nickels, dimes, and quarters, and then calculates change
    #if not enough money tell user how much money left they need and refund money
    cost = coffee_menu[command_console]["cost"]
    if total == cost:
        resources["money"] += cost
        return True
    elif total < cost:
        print("You have insufficient funds please try again")
        return False
    elif total > cost:
        print(f"Here is your change ${total - cost}")
        resources["money"] += cost
        return True


def make_coffee(drink):
    # if transaction is successful make coffee for user, and use up resources and then add money to machine
    if payment(coins, drink):
        ingredients_needed = coffee_menu[drink]["ingredients"]
        for item in ingredients_needed:
            if ingredients_needed[item] > resources[item]:
                print(f"Out of {item}")
                return
        print(f"Dispensing your {drink} Enjoy!")
        for item in ingredients_needed:
            resources[item] -= ingredients_needed[item]
    



 
while True:


    
    print("Welcome to the worlds best coffee machine... what would you like?(espresso($1.50), latte($2.50), cappuccino($3.00))")
    print("Type 'report' to check ingredient status")
    command_console = input().lower()


    if command_console == "report":
        report()
    elif command_console in coffee_menu:
        make_coffee(command_console)
    else:
        print("You are yapping right now")

    if command_console == "off":
        break

