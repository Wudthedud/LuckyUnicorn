def number_checker():
    while True:
        num = input("Please enter a number between 1 and 10: ")
        num = int(num)
        if 1 <= num <= 10:
            return num
        else:
            print("The number is not between 1 and 10. Please try again.")


print("You are playing with $" + str(number_checker()))
