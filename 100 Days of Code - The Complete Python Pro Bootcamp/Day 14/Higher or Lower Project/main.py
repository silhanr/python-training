import random, art
import sys

from game_data import data

def print_options(person_A,person_B):
    print(art.logo)
    print(f"Compare A: {person_A['name']}, {person_A['description']} from {person_A['country']}")
    print(art.vs)
    print(f"Against B: {person_B['name']}, {person_B['description']} from {person_B['country']}")

def get_input():
    try:
        player_input = input("Who has more followers? (A or B): ")
    except ValueError:
        print("Invalid type of input!")
        player_input = ""
    except:
        print("Invalid input!")
        player_input = ""

    if player_input == "A" or player_input == "B":
        return player_input

    return ""



def game():
    instagram_data = data
    random.shuffle(instagram_data)

    person_a = instagram_data.pop()
    person_b = instagram_data.pop()

    score = 0

    in_game = True
    while in_game:
        print_options(person_a,person_b)

        if person_a["follower_count"] >= person_b["follower_count"]:
            correct_person = "A"
        else:
            correct_person = "B"

        if get_input() == correct_person:
            score += 1
            print(f"You're right. Your current score is:{score}")
            person_a = person_b
            person_b = instagram_data.pop()
        else:
            in_game = False

    print(f"Sorry, that's wrong, your final score is {score}")

play_again = True
while play_again:
    game()
    play = input("Do you want to play again? (Y|N)").upper()

    if play != "Y":
        play_again = False