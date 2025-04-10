import random
import data
import art

print(art.logo)
def select_two_data(data_list, used_data):

    available_data = [item for item in data_list if item not in used_data]

    if len(data_list) < 2:
        return "Game Over", None, None

    item1 = random.choice(available_data)
    available_data_without_item1 = [item for item in available_data if item != item1]
    item2 = random.choice(available_data_without_item1)

    return None, item1, item2


def game():
    score = 0
    rounds = 5
    used_data = []
    for _ in range(rounds):
        game_over, item1, item2 = select_two_data(data.data, used_data)
        if game_over:
            print("No more unique items. Game Over!")
            break
        print(f"Compare A: {item1['name']}, {item1['description']}, from {item1['country']}.")
        print(art.vs)
        print(f"Against B: {item2['name']}, {item2['description']}, from {item2['country']}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if (guess == 'A' and item1['follower_count'] > item2['follower_count']) or \
           (guess == 'B' and item2['follower_count'] > item1['follower_count']):
            print("You're right!")
            score += 1
        else:
            print(f"Sorry, that's wrong.\n the {item1['name']} got {item1['follower_count']} and {item2['name']} got {item2['follower_count']}")
        used_data.extend([item1, item2])
    if score >= 3:
        print(f"You Win! Your score :{score}/{rounds}")
    else:
        print(f"You Loose! Your score :{score}/{rounds}")

game()

