# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside the function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside the function: {enemies}")


####     Without Using Global Variable   #####

import random
def game():
    compu_guess = random.randint(0,100)
    level = input(str("How challanging do you want the game to be?\n Hard(h) / Easy(e)  [Choose 'h' or 'e']\n"))

    if level == "h":
        guess = 5
    elif level == "e":
        guess = 10

    else:
        print("Invalid input")
    game_over = False

    while not game_over:
        if guess == 0:
            game_over = True
            print("You Loose")
            break
        user_guess = int(input(f"You got {guess} guesses remaning to guess the number.\n Make a guess ----> "))
        guess -= 1
        if user_guess == compu_guess:
            game_over = True
            print("You Won")

        elif user_guess > compu_guess:
            print("Too High")
        else:
            print("Too Low")

re = "y"
while re == "y":
    game()
    re = input(f"Do you wanna re-play this game? \n Type 'y' to continue\n -->")




