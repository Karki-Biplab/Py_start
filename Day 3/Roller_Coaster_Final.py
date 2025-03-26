#################### Day 3 (IF/ELSE/Nested) ###################

print("Welcome to the Roller Coaster")
height = int(input("What is your height in CM? "))
bill = 0

if height >= 120:
    print("Jau babu khela moz gara ")
    age = int(input("What is your age? "))
    if age<12:
        bill = 5
        print("Chup lagera $5 tir fuchey.")
    elif age<18:
        bill = 7
        print("Chup lagera $7 tir vai")
    elif age >=45 and age <=55:
        bill = 0
        print("Tero Jindagi mozz vayxa aba sittai ma khel budo")

    else:
        bill = 10
        print("ohooo tir vai $10 ta ta thulo vai sakexas")


    photo = input("tero photo Khichney ki nai? Y/N. ")
    if photo == "Y":
        bill +=3

    print(f"Tailey ${bill} tirna paryo total tso vaye ")

else:
    print("Thait, jau paila complain khau ani height badhesi aau khelna lai ")
