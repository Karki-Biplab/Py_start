##Number Sign:Write a program that takes a number as input and prints whether it's positive, negative, or zero.
# try:
#     num = float(input("Enter the number that you wanna check wether it is negative, positive or a Zer0 --> "))
#     if num < 0:
#         print(f" {num} is negative")
#     elif num == 0:
#         print(f" {num} is Zero")
#     else:
#         print(f" {num} is Poitive")
# except ValueError:
#     print("Invalid Input")


##Grading System:Write a program that takes a student's score as input and prints their corresponding grade
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60.
# try:
#     mark = float(input("What mark did you just got in the exams? "))
#     if mark >= 90 and mark <= 100:
#         print("You just got an A.")
#     elif mark >= 80:
#         print("you just got a B ")
#     elif mark >= 70:
#         print("you just got a C ")
#     elif mark >= 60:
#         print("you just got a D ")
#     else:
#         print("youre fail")
#
# except ValueError:
#     print("Please enter a Valid Mark in Numbers")




##Sum of Numbers:Write a for loop that calculates the sum of numbers from 1 to 10.

# sum = 0
# for num in range(1,11):
#     sum += num
#     print(sum)

##Countdown:Write a while loop that counts down from 10 to 1 and prints each number.

num = 10
while num != 0:
    print(num)
    num = num -1
