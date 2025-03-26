#################### Day 3 (IF/ELSE/Nested) ###################

print("Welcome to the Roller Coaster")
height = int(input("What is your height in CM? "))
if height >= 120:
    print("Jau babu khela moz gara ")
    age = int(input("What is your age? "))
    if age<12:
        print("Chup lagera $5 tir fuchey.")
    elif age<18:
        print("Chup lagera $7 tir vai")
    elif age >=18:
        print("ohooo tir vai $10 ta ta thulo vai sakexas")
else:
    print("Thait, jau paila complain khau ani height badhesi aau khelna lai ")