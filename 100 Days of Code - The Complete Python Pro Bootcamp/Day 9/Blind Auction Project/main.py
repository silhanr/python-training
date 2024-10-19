# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

print(logo)

another_bid = "yes"
auction = {}

while another_bid == "yes":
    name = input("Insert name:")
    bid = input("Your bid: $")

    auction[name] = int(bid)

    another_bid = input("Other bid users? (yes/no)")

max_bid = max(auction.values())

for key in auction:
    if auction[key] == max_bid:
        print(f"Max bid was placed by {key} with ${auction[key]}")
