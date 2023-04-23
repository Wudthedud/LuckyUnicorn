def number_checker():
    num = int(input("Choose a number between 1-10"))
    if 1 <= num <= 10:
        return True
    else:
        return False


print(number_checker())
