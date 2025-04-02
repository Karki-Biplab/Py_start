# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A peice of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again.",
# }
#
# #Retrieving items from dictionary.
# print(programming_dictionary)

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
#
# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
# for name in student_scores:
#     scores = student_scores[name]
#
#     if scores >= 91:
#         grade = ("Outstanding")
#     elif scores >= 81:
#         grade = ("Exceeds Expectations")
#     elif scores >= 71:
#         grade = ("Acceptable")
#     else:
#         grade = ("Fail")
#     student_grades[name] = grade
#
# # TODO-2: Write your code below to add the grades to student_grades.👇
#
#
# # 🚨 Don't change the code below 👇
# print(student_grades)

####   Nesting    #####
# travel_log = {
#     "France": {"cities_visited":["Paris", "Lille", "Dijon"]},
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }
#
# cities_visited = travel_log["France"]
# print(travel_log)

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above
#
# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country, visits, cities):
#     global travel_log
#     new_country_data = {
#     "country" : country,
#     "visits" : visits,
#     "cities" : cities
#     }
#     travel_log.append(new_country_data)
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# import clear
# from art import logo
# print(logo)
redo = "Y"
new_data = {}


while redo == "Y":
    name = input("What is your name?")
    price = int(input("What is your bid amount? $"))
    redo = input("is there more bider? Y/N")
    new_data[name] = price


max_amt = 0
max_bider = ""
if name in new_data:
    bid = new_data[name]
    if max_amt < bid:
        max_amt = bid
        max_bider = name

print(f"The Winner Bidder is {max_bider} with a bid of ${max_amt}")



