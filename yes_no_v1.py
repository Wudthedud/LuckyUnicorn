def yes_no(question):
    answer = input(question + "(Y/N")
    if answer == "yes":
        return True
    elif answer == "no":
        return False


yes_no("Have you played this game before")
