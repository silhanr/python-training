import random

NUM = random.randint(1,100)
EASY_LEVEL = 10
HARD_LEVEL = 5
def level_choice():
    level = input("Choose your level [easy, hard]:\n").lower()
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def check_guess(number):
    if number == NUM:
        return True
    elif number < NUM:
        print("Too low")
        return False
    else:
        print("Too high")
        return False

def game():
    remaining_guesses = level_choice()

    guess = -1

    while remaining_guesses > 0 and guess != NUM:
        guess = int(input(f"Guess number - ({remaining_guesses} attempts): "))
        if check_guess(guess):
            print(f"You win, guessed number was {NUM}")
            break
        else:
            remaining_guesses -= 1

    if remaining_guesses == 0:
        print(f"You lose, guessed number was {NUM}")

game()