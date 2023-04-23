import random


def generate():
    token = ['U', 'Z', 'H', 'D']
    return random.choice(token)


print(generate())
