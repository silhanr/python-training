print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# if pepperoni == "Y":
#     add_pepperoni = True
# else:
#     add_pepperoni = False
#
# if extra_cheese == "Y":
#     add_cheese = True
# else:
#     add_cheese = False
price = 0

if size == "S":
    price += 15
elif size == "M":
    price += 20
elif size == "L":
    price += 25
else:
    pass

if pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price}.")
