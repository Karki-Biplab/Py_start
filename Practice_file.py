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

# num = 10
# while num != 0:
#     print(num)
#     num = num -1


######Day-2
# Beginner-Level Loop Exercises:
# Multiplication Table:
# Write a program that takes a number as input and prints its multiplication table from 1 to 10.
# try:
#     usr_num = int(input("What number's multiplication  table do you want?\n "))
#     def mul_table():
#         num = 1
#         mul_table = False
#         while num <= 10:
#             if num <= 1:
#                 mul_table = True
#             table = usr_num * num
#             print(f"{usr_num} x {num} = {table} ")
#             num = num + 1
#
#     mul_table()
#
# except ValueError:
#     print("I think you entred the wrong form of input")




# Even Numbers:
# Write a program that prints all even numbers between 1 and 20 (inclusive).
#for num in range(1,21):
num = 1
while num <= 20:
        even = num % 2
        if even == 0:
                print(f"{num}")
        num = num + 1



# Reverse String:
# Write a program that takes a string as input and prints it in reverse order.



# Factorial:
# Write a program that takes a non-negative integer as input and calculates its factorial (e.g., 5! = 5 * 4 * 3 * 2 * 1).



# Pattern Printing (Simple):
# Write a program that prints the following pattern:
# \*
# \*\*
# \*\*\*
# \*\*\*\*
# \*\*\*\*\*


