def yes_no(question):
    answer = input(question + " (Y/N): ").strip().lower()
    if answer == "yes" or answer == "y":
        return True
    elif answer == "no" or answer == "n":
        return False
    else:
        print("Invalid input. Please enter 'yes' or 'no'")


print(yes_no("Have you played this game before"))