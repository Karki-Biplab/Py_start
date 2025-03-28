########################### Day 5 (Loops) ##########################

for number in range(0, 101):
    if number % 15 == 0:
        print(number)
        print("fizz")
        print("buzz")
    elif number % 3 == 0:
        print(number)
        print("fizz")
    elif number % 5 ==0:
        print(number)
        print("buzz")