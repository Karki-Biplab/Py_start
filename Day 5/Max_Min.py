########################### Day 5 (Loops) ##########################

print("Welcome to the Minimum and maximum number finder")
numbers = input("Please write down the numbers with comma seperating them ")
sep_numbers = numbers.split(",")  #1,2,3,4
max_num = int(sep_numbers[0])
min_num = int(sep_numbers[0])

for number in sep_numbers:
    number = int(number)
    if number > max_num:
        max_num = number

    if number < min_num:
        min_num = number

print( f"the maximum number in the list is {max_num} and minimum is {min_num}")