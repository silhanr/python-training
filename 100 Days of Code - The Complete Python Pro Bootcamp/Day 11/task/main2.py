import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
states = (0,1,2)

def print_board(player_deck, pc_deck, show_pc_deck):
    print("*******************************************")
    print(f"Your cards are: {player_deck} = {sum(player_deck)}")
    if show_pc_deck:
        print(f"PC's cards are: {pc_deck} = {sum(pc_deck)}")
    else:
        print(f"PC's cards are: [{pc_deck[0]}]")
    print("*******************************************")

def evaluate(player_deck, pc_deck, show_pc_deck: bool):
    print_board(player_deck, pc_deck, show_pc_deck)

    if not check_deck(player_deck):
        print(f"\n##########################\nYou lose\n##########################")
    elif sum(player_deck) == 21 and sum(pc_deck) != 21:
        # Instant win
        print(f"\n##########################\nYou win\n##########################")
    elif sum(pc_deck) == 21:
        # PC has 21
        print(f"\n##########################\nYou lose\n##########################")
    elif sum(player_deck) == sum(pc_deck):
        print(f"\n##########################\nDraw\n##########################")
    elif check_deck(pc_deck) and sum(player_deck) < sum(pc_deck):
        print(f"\n##########################\nYou lose\n##########################")
    else:
        print(f"\n##########################\nYou win\n##########################")


def check_deck(deck_of_cards: list):
    """
    Checks whether the deck of cards is still in game and converts Ace to 1 if needed
    :param deck_of_cards:
    :return: False if sum of cards exceeds 21
    """
    # print(sum(deck_of_cards))
    if sum(deck_of_cards) > 21:
        if 11 in deck_of_cards:
            deck_of_cards[deck_of_cards.index(11)] = 1
            return check_deck(deck_of_cards)
        else:
            return False
    else:
        return True


def take_card(deck_of_cards: list):
    decision = input(f"Do you want another card? (y/n):\n")
    if decision == "y":

        deck_of_cards.append(random.choice(cards))
        return True
    elif decision != "n":
        print("Unrecognized options!")
        return take_card(deck_of_cards)
    else:
        return False

def pc_takes_card(deck_of_cards: list):
    if sum(deck_of_cards) < 17:

        deck_of_cards.append(random.choice(cards))
        return True
    else:
        return False

def game():
    print(logo)

    player_deck = [random.choice(cards), random.choice(cards)]
    pc_deck = [random.choice(cards), random.choice(cards)]
    show_pc_deck = False



    player_continues = True
    while player_continues and check_deck(player_deck):
        print_board(player_deck, pc_deck, show_pc_deck)
        player_continues = take_card(player_deck)



    pc_continues = True
    while not sum(player_deck) > 21 and pc_continues and check_deck(pc_deck):
        show_pc_deck = True
        pc_continues = pc_takes_card(pc_deck)
        print_board(player_deck, pc_deck, show_pc_deck)

    evaluate(player_deck,pc_deck,show_pc_deck)

while input("Play blackjack?: ") == "y":
    game()