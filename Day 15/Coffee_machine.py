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


def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources.get(item, 0):
            print(f"Sorry, not enough {item}.")
            return False
    return True


def make_coffee(coffee_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {coffee_name}. Enjoy!")


def dispensor():
    coffee_input = input("What do you wanna have? ('espresso'/'latte'/'cappuccino'): ").lower()

    if coffee_input not in MENU:
        print("Invalid selection.")
        return

    drink = MENU[coffee_input]
    if check_resources(drink["ingredients"]):
        print(f"The cost is ${drink['cost']}")
        make_coffee(coffee_input, drink["ingredients"])


dispensor()
