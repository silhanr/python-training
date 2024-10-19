import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_chars = [nr_letters,nr_symbols,nr_numbers]
all_chars = [letters,symbols,numbers]



password = ""
char = 0
while sum(total_chars) > 0:
    type_of_char = random.randint(0,2)
    # print(all_chars[type_of_char])
    if total_chars[type_of_char] > 0:
        password += all_chars[type_of_char][random.randint(0,len(all_chars[type_of_char])-1)]
        total_chars[type_of_char] -= 1

    # print(sum(total_chars))
    # print(total_chars)
    # print(password)
print(password)