"""
Lucky Unicorn Final Version
By Daniel Wu
"""
import random

balance = 10


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
            if 1 <= num <= balance:
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


# Farewell Message
def farewell():
    print("============ Thanks for playing ============= \n"
          "\t You started with $10 \n"
          f"\t You finished with {balance} \n"
          "Goodbye \n"
          "=============================================")


# Main Code

# Welcome screen, asking if they have played before and if no, showing them the payout amount and other information
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
        print(f"You finished with a balance of ${balance} after {rounds} rounds.")
        farewell()
        exit()

# Round calculation
print(f"You ran out of money after {rounds} rounds")
farewell()
