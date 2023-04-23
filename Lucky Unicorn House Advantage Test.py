"""
Lucky Unicorn Final Version
CHECKING FOR HOUSE ADVANTAGE IN TOKEN GENERATION
By Daniel Wu
"""
import random


# Yes/No Checker
def yes_no(question):
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
    print("============ Welcome to Lucky Unicorn ============= \n"
          "Price per round: $1 \n"
          "\t Payout Rewards: \n"
          "\t Unicorn: $5 \n"
          "\t Zebra: $0.5 \n"
          "\t Horse: $0.5 \n"
          "\t Donkey: $0 \n"
          "Try to avoid donkeys, get the unicorns, and finish with more money than you started with. \n"
          "===================================================")


# Number checker
def number_checker():
    while True:
        num = input("Please enter how much you want to bet: ")
        try:
            num = int(num)
            if 1 <= num <= 10 and num <= balance:
                print("You are playing with $" + str(num))
                return num
            else:
                print("The number is not between 1 and 10, or is larger than your current balance. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Token generator
def generate():
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


# Main Code
balance = 100
rounds = 0
while balance > 0:
    amount = 5
    balance -= amount
    balance += generate() * amount
    rounds += 1
    print(f"You now have ${balance}")
else:
    print(f"You finished with a balance of ${balance} after {rounds} rounds.")
    exit()

