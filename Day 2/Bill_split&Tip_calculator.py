#########DAY 2##########

# numbe = input("Enter the number you wanna add= ")
# print(int(numbe[0]) + int(numbe[1]))

# print(round(8/3, 2))
# print(8//3)

# print("Welcome to the tip calculator")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill? "))
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# print(f"Each person should pay: ${final_amount}")

print("Welcome to the Tip and bill calculator. ")
bill = float(input("What was the total bill?  $"))
tip = input("What percentage of tip would like to give? 10, 12,15......? ")
tip_amount = int(bill) * int(tip) /100
print(f"you gonna tip  {tip_amount}")
total_bill = int(bill) + int(tip_amount)
people = input("How many people are there to split? ")
personal_bill = total_bill // int(people)
print(f" Your total bill is {total_bill} and each person should pay {personal_bill} ")