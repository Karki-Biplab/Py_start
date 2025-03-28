########################### Day 5 (Loops) ##########################

#Password Generator Project
import random
print("Welcome to the Password Generator")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

usr_letters= int(input("How many letters would you like in your password?\n"))
usr_symbols = int(input(f"How many symbols would you like?\n"))
usr_numbers = int(input(f"How many numbers would you like?\n"))
passw = ""
for letter in range(0, usr_letters):
    rand_letter = random.choice(letters)
    passw += rand_letter
    print(passw)

for number in range(0, usr_numbers):
    rand_number = random.choice(numbers)
    passw += rand_number
    print(passw)

for symbol in range(0, usr_symbols):
    rand_symbol = random.choice(symbols)
    passw += rand_symbol
    print(passw)

password = ''.join(random.sample(passw, len(passw)))
print(password)