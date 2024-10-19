import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_guess = int(input("What do you choose? Type 0 - Rock, 1 - Paper, 2 - Scissors: "))
pc_guess = random.randint(0,2)

guesses = [rock,paper,scissors]


if player_guess == pc_guess:
    print("Draw")
elif player_guess == 0 and pc_guess == 1:
    print("PC wins")
elif player_guess == 1 and pc_guess == 2:
    print("PC wins")
elif player_guess == 2 and pc_guess == 0:
    print("PC wins")
else:
    print("Player wins")

print(f"Player: {guesses[player_guess]}")
print(f"PC: {guesses[pc_guess]}")
