"""
Lucky Unicorn Version 4 (Component 3 - Token Generation)
Generates token and calculates payout
By Daniel Wu
"""
import random


# Yes/No Checker
def yes_no(question):
    while True:
        answer = input(question + " (Y/N): ").strip().lower()
        if answer == "yes" or answer == "y":
            return True
        elif answer == "no" or answer == "n":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'")


# Instructions
def instructions():
    print("============ Welcome to Lucky Unicorn ============= \n"
          "Price per round: $1 \n"
          "\t Payout Rewards: \n"
          "\t Unicorn: $5 \n"
          "\t Zebra: $0.5 \n"
          "\t Horse: $0.5 \n"
          "\t Donkey: $0 \n"
          "Try to avoid donkeys, get the unicorns, and finish with more money than you started with. \n"
          "===================================================")


def generate():
    token_list = ["U", "Z", "H", "D"]

    token = random.choice(token_list)
    if token == "U":
        token_name = "Unicorn Token"
        prize = 5
    elif token == "Z":
        token_name = "Zebra Token"
        prize = 0.5
    elif token == "H":
        token_name = "Horse Token"
        prize = 0.5
    else:
        token_name = "Donkey Token"
        prize = 0
    print(f"You got a {token_name}!")
    return prize


# Main Code
if yes_no("Have you played this game before"):
    pass
else:
    instructions()

if not yes_no("Confirm the payment of $1?"):
    print("Exit program")
    exit()

generate()
