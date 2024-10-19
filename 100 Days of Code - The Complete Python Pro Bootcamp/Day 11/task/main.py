import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
states = (0,1,2)

def print_board(player_deck, pc_deck, show_pc_deck):
    print(f"Your cards are: {player_deck}")
    if show_pc_deck:
        print(f"PC's cards are: {pc_deck}")
    else:
        print(f"PC's cards are: [{pc_deck[0]}]")

def print_winner(player_deck, pc_deck, show_pc_deck: bool):
    if sum(player_deck) == 21:
        # Instant win
        print(f"\n##########################\nYou win\n##########################")
    elif sum(player_deck) < 21 and sum(player_deck) > sum(pc_deck):
        # Player has higher sum
        print(f"\n##########################\nYou win\n##########################")
    elif sum(player_deck) == sum(pc_deck) < 21:
        print(f"\n##########################\nDraw\n##########################")
    else:
        print(f"\n##########################\nYou lose\n##########################")
    print_board(player_deck,pc_deck,show_pc_deck)

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


def take_card(deck_of_cards: list,opponent_cards):
    print_board(deck_of_cards,opponent_cards,False)
    if check_deck(deck_of_cards):
        decision = input(f"Do you want another card? (y/n):\n")
        if decision == "y":
            deck_of_cards.append(random.choice(cards))
            return take_card(deck_of_cards,opponent_cards)
        elif decision == "n":
            return True
        else:
            print("Unrecognized options!")
            return take_card(deck_of_cards,opponent_cards)
    else:
        return False

def pc_takes_card(deck_of_cards: list,opponent_cards):
    print_board(opponent_cards,deck_of_cards, True)
    if check_deck(deck_of_cards):
        if sum(deck_of_cards) < 17:
            deck_of_cards.append(random.choice(cards))
            return pc_takes_card(deck_of_cards,opponent_cards)
        else:
            return True
    else:
        return False

# Main program
print(logo)

player_deck = [random.choice(cards), random.choice(cards)]
pc_deck = [random.choice(cards), random.choice(cards)]


show_pc_deck = False

print_board(player_deck,pc_deck,show_pc_deck)


if sum(player_deck) == 21:
    # Instant win
    pass

elif take_card(player_deck,pc_deck):
    show_pc_deck = True
    if pc_takes_card(pc_deck,player_deck):
        # Game ends - evaluate result
        pass
    else:
        # PC exceeded 21, Player wins
        pass
else:
    # Player exceeded 21, PC wins
    pass
print_winner(player_deck,pc_deck,show_pc_deck)

