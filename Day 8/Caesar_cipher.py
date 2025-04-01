# def greet():
#      print("Hello")
#      print("Hello")
#      print("Hello")
#
# greet()

# def greet(sth):
#      print(sth)
#      # print("Hello")
#      # print("Hello")
#
# greet("namaste")

# #function with more than 1 input
# def info(name, location):
#      print(f"Hello {name}")
#      print(f"what's new in {location}")
#
# name = input("your name ")
# location = input("Where are you from? ")
# info(name, location)

#Functions with keyword arguments
# def info(name, location):
#      print(f"Hello {name}")
#      print(f"what's new in {location}")
#
# info(location="guuuuuuu", name="pujooo")


### Area Calculation ###############
# import math
# def area_calc(h, b, c):
#      num_can =  (h * b)/c
#      ac_num_can = math.ceil(num_can)
#      print(f"you gonna need {num_can} of paints to paint but you have to buy {ac_num_can} cans of paint")
#
# h = int(input("What is the Height if the wall?  "))
# b = int(input("What is the Width if the wall?  "))
# c = int(input("What is the Coverage if the wall?  "))
# area_calc(h, b, c)

### Prime Number Checker ####

# def prime_checker(num):
#      for numb in range(2, num):
#           if num%numb == 0:
#                print("This is not a prime number")
#                return False
#      print("Is Prime")
#
# num = int(input("Check the number: "))
# prime_checker(num)
#
# ###### Caesar Cipher 1 #########
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# def encrypt(text, shift):
#     enco_txt = ""
#     for i in range(0, len(text)):
#         letter = text[i]
#         enco_index = alphabet.index(letter)+shift
#         if enco_index > 25:
#             enco_index = enco_index - 26
#         enco_txt += alphabet[enco_index]
#     print((enco_txt))
# encrypt(text, shift)


# ###### Caesar Cipher 2 #########
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")
#
# def decrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         if new_position < 0:
#             new_position = new_position +26
#         cipher_text += alphabet[new_position]
#     print(f"The decoded text is {cipher_text}")
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# else:
#     decrypt(plain_text=text, shift_amount=shift)



# # ###### Caesar Cipher Final #########
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# def caeser(plain_text, shift_amount, direction):
#       cipher_text = ""
#       for letter in plain_text:
#           position = alphabet.index(letter)
#           if direction == "encode":
#               new_position = position + shift_amount
#           elif direction == "decode":
#               new_position = position - shift_amount
#           cipher_text += alphabet[new_position]
#       print(f"The {direction}d text is {cipher_text}")
#
# caeser(text, shift, direction)


# ###### Caesar Cipher Complete #########
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")


# TODO-1: Import and print the logo from art.py when the program starts.
print(art.logo)
# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
re_run = "Yes"
while re_run.lower() == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    # Hint: Think about how you can use the modulus (%).

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    re_run = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")


