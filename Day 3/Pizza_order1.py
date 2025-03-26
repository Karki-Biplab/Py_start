#################### Day 3 (IF/ELSE/Nested) ###################

# #########pizzaa Order######
print("Lu garam Aba Mitto pizza khana lai order")
bill = 0
size = input("Katro Pizza khanxes? S, M, L -->")
if size == "S":
    bill =15
elif size == "M":
    bill =20
elif size == "L":
    bill =25
add_pepperoni = input("Pepperoni halni vaye extra lagxa.  Y/N  --> ")
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
add_cheese = input("Extra Cheese ni halne ho? Y/N --> ")
if add_cheese == "Y":
    bill += 1
    print(f"Tero pizza ko total bill ${bill} hunxa")
else:
    print(f"Tero pizza ko total bill ${bill} hunxa")