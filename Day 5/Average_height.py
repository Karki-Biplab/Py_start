########################### Day 5 (Loops) ##########################
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + "Pie")
# print(fruits)

print("Welcome to the Average Height Calculator")
stud_heights = input("Please write down the height of the students with comma seperating them ")
heights = stud_heights.split(",")
tot_height = 0
length = 0
for height in heights:
    tot_height += int(height)
    length += 1
    avg_height = tot_height//length
print( f"Acc to the heights of your students, the average comes of {avg_height}")