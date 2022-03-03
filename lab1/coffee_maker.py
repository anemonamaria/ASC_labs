"""
A command-line controlled coffee maker.
"""

import sys
import load_recipes
"""
Implement the coffee maker's commands. Interact with the user via stdin and print to stdout.

Requirements:
    - use functions
    - use __main__ code block
    - access and modify dicts and/or lists
    - use at least once some string formatting (e.g. functions such as strip(), lower(),
    format()) and types of printing (e.g. "%s %s" % tuple(["a", "b"]) prints "a b"
    - BONUS: read the coffee recipes from a file, put the file-handling code in another module
    and import it (see the recipes/ folder)

There's a section in the lab with syntax and examples for each requirement.

Feel free to define more commands, other coffee types, more resources if you'd like and have time.
"""

"""
Tips:
*  Start by showing a message to the user to enter a command, remove our initial messages
*  Keep types of available coffees in a data structure such as a list or dict
e.g. a dict with coffee name as a key and another dict with resource mappings (resource:percent)
as value
"""

# Commands
EXIT = "exit"
LIST_COFFEES = "list"
MAKE_COFFEE = "make"  #!!! when making coffee you must first check that you have enough resources!
HELP = "help"
REFILL = "refill"
RESOURCE_STATUS = "status"
commands = [EXIT, LIST_COFFEES, MAKE_COFFEE, REFILL, RESOURCE_STATUS, HELP]

# Coffee examples
ESPRESSO = "espresso"
AMERICANO = "americano"
CAPPUCCINO = "cappuccino"
COFFEES = [ESPRESSO, AMERICANO, CAPPUCCINO]
# Resources examples
WATER = "water"
COFFEE = "coffee"
MILK = "milk"

# Coffee maker's resources - the values represent the fill percents
RESOURCES = {WATER: 100, COFFEE: 100, MILK: 100}

COFFEE_RESOURCES = {ESPRESSO: {WATER: 5, COFFEE: 10, MILK: 0},
                AMERICANO: {WATER: 10, COFFEE: 10, MILK: 0},
                CAPPUCCINO: {WATER: 5, COFFEE: 10, MILK: 10}}
"""
Example result/interactions:

I'm a smart coffee maker
Enter command:
list
americano, cappuccino, espresso
Enter command:
status
water: 100%
coffee: 100%
milk: 100%
Enter command:
make
Which coffee?
espresso
Here's your espresso!
Enter command:
refill
Which resource? Type 'all' for refilling everything
water
water: 100%
coffee: 90%
milk: 100%
Enter command:
exit
"""

def show_coffees(coffees):
    for coff in coffees:
        print("---" + coff)
    print()

def show_status(status):
    for stat in status:
        print("current status for " + stat + " is ", status[stat])
    print()

def make_coffee(coffee):
    make = 1
    # for coff in COFFEES:
    if coffee not in COFFEES:
        make = 0
        print("Sorry, we don't have this product")
            # checks if the coffee is in our product list
            # break

    enough_resources = 1
    if make == 1:
        # print(COFFEE_RESOURCES[AMERICANO][WATER])
        for i in RESOURCES:
            if RESOURCES[i] < COFFEE_RESOURCES[coffee][i]:
                enough_resources = 0;
                print("We don't have enough resources. Please wait a sec.")
                break;
        if enough_resources == 1:
            for res in RESOURCES:
                RESOURCES[res] = RESOURCES[res] - COFFEE_RESOURCES[coffee][res]
            print("Coffee ready! Good to go!")

def refill_resource(your_resource):
    if your_resource == "all":
        for res in RESOURCES:
            # print(res)
            RESOURCES[res] = 100
        show_status(RESOURCES)
    elif your_resource == "water" or your_resource == "coffee" or your_resource == "milk":
        RESOURCES[your_resource] = 100
        show_status(RESOURCES)
    else:
        print("Please introduce a valid resource")


print("I'm a simple coffee maker")
print("Press enter to see available commands")
# load_recipes.show_recipe("americano")
# sys.stdin.readline()
# print("Teach me how to make coffee...please...")
if __name__ == "__main__":
    print(commands)

    while 1:
        print("What do you want me to do?")
        your_command = sys.stdin.readline().strip()

        if your_command == LIST_COFFEES:
            print("we have ")
            show_coffees(COFFEES)
        elif your_command == RESOURCE_STATUS:
            show_status(RESOURCES)
        elif your_command == EXIT:
            print("BYE BYE")
            break
        elif your_command == MAKE_COFFEE:
            print("Which coffee?")
            your_coffee = sys.stdin.readline().strip()
            make_coffee(your_coffee)
        elif your_command == REFILL:
            print("Which resource to refill?")
            your_resource = sys.stdin.readline().strip()
            refill_resource(your_resource)

        else:
            print("Please introduce a valid command.")