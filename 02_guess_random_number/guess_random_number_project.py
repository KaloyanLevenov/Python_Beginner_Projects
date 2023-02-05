import random


def guess_func(number):
    print("Your mighty PC picked a number between 1 and 365. Your job is to find out that number.\n Luckily your PC will give you some hints during this journey. Good Luck!")
    random_number = random.randint(1, number)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter your guess number between 1 and {number}: "))

        if guess < random_number:
            if guess < (random_number * 10):
                print("Huh.... You're too low. Guess again.")
            print("You're pretty close. However it is low...... Or may be you are not pretty close. TRY AGAIN!")
        elif guess > random_number:
            if guess > (random_number * 10):
                print("Huh.... You're too high. Guess again.")
            print("Two feet above the ground..... yet high. TRY AGAIN!")

    print(f"Congratulations, even though I expected to make it faster.\n You've guessed my number {random_number}!")


def computer_guess(number):
    print("Table has turned! Think of a number between 1 and 365 and help the computer to guess your number.\n Have fun!!!")
    low = 1
    high = number
    feedback_from_user = ""
    while feedback_from_user != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback_from_user = input(f"Is {guess} high (H), or low (L) or correct (C)??").lower()
        if feedback_from_user == 'h':
            high = guess - 1
            guess = random.randint(low, high)
        elif feedback_from_user == 'l':
            low = guess + 1
    print(f"The computer guessed your number, {guess}, correctly!")



guess_func(365)
computer_guess(365)
