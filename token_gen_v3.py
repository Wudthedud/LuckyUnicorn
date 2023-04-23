import random


def generate():
    token_name = ""
    prize = 0
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
    print(f"You got a {token_name}!")
    return prize



print("Payout: $" + str(generate()))
