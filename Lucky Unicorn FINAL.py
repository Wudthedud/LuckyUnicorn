"""
Lucky Unicorn Final Version.

By Daniel Wu
"""

import random
starting_balance = 10
balance = starting_balance


# Yes/No Checker
def yes_no(question):
    """Check whether the answer to a question is yes/no."""
    while True:
        answer = input(question + " (Y/N): \n").strip().lower()
        if answer == "yes" or answer == "y":
            return True
        elif answer == "no" or answer == "n":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'")


# Instructions
def instructions():
    """Display information about the game for the user."""
    print("============ Welcome to Lucky Unicorn ============= \n"
          "Price per round: $1 \n"
          "\t Payout Rewards: \n"
          "\t Unicorn: 3x your bet \n"
          "\t Zebra: 1/2 your bet \n"
          "\t Horse: 1/2 your bet \n"
          "\t Donkey: Nothing :( \n"
          "Try to avoid donkeys, get the unicorns, and finish with "
          "more money than you started with. \n"
          "===================================================")


# Number checker
def number_checker():
    """Check whether the input is a number between selected values."""
    while True:
        num = input("Please enter how much you want to bet: ")
        try:
            num = int(num)
            if 1 <= num <= balance:
                print("You are playing with $" + str(num))
                return num
            else:
                print("The number is not between 1 and 10, or is larger "
                      "than your current balance. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Token generator
def generate():
    """Generate the token and links to price."""
    token_list = ["U", "Z", "H", "D"]

    token = random.choice(token_list)
    if token == "U":
        token_name = "Unicorn Token"
        prize = 3
    elif token == "Z":
        token_name = "Zebra Token"
        prize = 0.5
    elif token == "H":
        token_name = "Horse Token"
        prize = 0.5
    else:
        token_name = "Donkey Token"
        prize = 0
    print(f"You got a {token_name}, that means you get ${prize * amount}")
    return prize


# Farewell Message
def farewell():
    """Display Farewell message and summary of their game."""
    print("============ Thanks for playing ============= \n"
          f"\t You started with ${starting_balance} \n"
          f"\t You finished with ${balance} \n"
          "Goodbye \n"
          "=============================================")


# Main Code

# Welcome screen, asking if they have played before and if no
# showing them the payout amount and other information
if yes_no("Have you played this game before?"):
    pass
else:
    instructions()

# This is where the user gets to pick how much they want to bet
amount = number_checker()

# Confirming that amount
if not yes_no(f"Confirm the payment of ${amount}?"):
    print("Quitting the game...")
    farewell()
    exit()

# Calculating the balance
balance -= amount
balance += generate() * amount
print(f"You now have ${balance}")
rounds = 1
while balance >= 1:
    if yes_no("Do you want to play again? \n"):
        amount = number_checker()
        balance -= amount
        balance += generate() * amount
        rounds += 1
        print(f"You now have ${balance}")
    else:
        print(f"You finished with a balance of"
              f" ${balance} after {rounds} rounds.")
        farewell()
        exit()

# Round calculation
print(f"You ran out of money after {rounds} rounds")
farewell()
