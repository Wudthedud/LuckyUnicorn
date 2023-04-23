"""
Lucky Unicorn Version 2
Yes/No Checker
By Daniel Wu
"""


def yes_no(question):
    while True:
        answer = input(question + "(Y/N").strip().lower()
        if answer == "yes":
            return True
        elif answer == "no":
            return False


def instructions():
    print("============ Welcome to Lucky Unicorn ============= \n"
          "Price per round: $1 \n"
          "\t Payout Rewards: \n"
          "\t Unicorn: $5 \n"
          "\t Zebra: $0.5 \n"
          "\t Horse: $0.5 \n"
          "\t Donkey: $0 \n"
          "===================================================")


instructions()
