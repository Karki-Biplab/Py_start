#################### Day 3 (IF/ELSE/Nested) ###################

print("Welcome to the Love Calculator")
name1 = input("hal tero Girlfriend vanaudi  ko nam ")
name2 = input("Ani babu timro nam xai kosle halxa? lekh ya  ")

let_tru = 0
let_lov = 0

low_name = name1 + name2

#First persrnt ko number nikalna lai ho yo
let_tru += low_name.count("t") + low_name.count("r") + low_name.count("u") + low_name.count("e")


#Second percent ko number nikalna lai ho yo
let_lov += low_name.count("l") + low_name.count("o") + low_name.count("v") +low_name.count("e")
let1 = str(let_tru)
let2 = str(let_lov)
percent = int(let1 + let2)

if percent <=10 or percent >=90:
    print(f"timmi haru ko jodi {percent}% mileko xa matlab coke ra mentos jasto")
elif percent >40 and percent <50:
    print(f"timmi haru ko jodi {percent}% mileko xa Tathasthu ")
else:
    print(f"timmi haru ko jodi {percent}% mileko xa Bichar garnu ")

