import random


def generate():
    token_name = ""
    token_list = ["U", "Z", "H", "D"]

    token = random.choice(token_list)
    if token == "U":
        token_name = "Unicorn"
    elif token == "Z":
        token_name = "Zebra Token"
    elif token == "H":
        token_name = "Horse Token"
    else:
        token_name = "Donkey Token"



print(generate())
