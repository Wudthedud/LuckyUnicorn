"""
Lucky Unicorn Version 6 (Component 7 - Feedback and looping)
Loops while they have more than $0 and tells them how many rounds they played
By Daniel Wu
"""
import random

balance = 10


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
    print(f"You got a {token_name}, that means you get ${prize}")
    return prize


# Main Code
if yes_no("Have you played this game before"):
    pass
else:
    instructions()

if not yes_no("Confirm the payment of $1?"):
    print("Exit program")
    exit()

balance -= 1

balance += generate()
print(f"Your remaining balance is: ${balance}")
rounds = 1
while balance > 0:
    if yes_no("Do you want to play again?"):
        balance -= 1
        balance += generate()
        rounds += 1
        print(f"Your remaining balance is: ${balance}")
    else:
        print(f"You finished with a balance of ${balance} after {rounds} rounds.")
        exit()
print(f"You ran out of money after {rounds} rounds")
