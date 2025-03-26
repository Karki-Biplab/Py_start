#################### Day 3 (IF/ELSE/Nested) ###################

########LeapYear######

year = int(input("Enter the year you wanna check if it's a leap year or not: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a Leap Year!")
        else:
            print(year, "is NOT a Leap Year.")
    else:
        print(year, "is a Leap Year!")
else:
    print(year, "is NOT a Leap Year.")