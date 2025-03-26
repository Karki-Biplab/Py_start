#################### Day 3 (IF/ELSE/Nested) ###################

print("Welcome to the BMI Calculator")
height = float(input("What is your Height in Meters ? "))
weight = float(input("What is your Weiht in KiloGram ? "))
bmi = weight / height ** 2
if bmi < 18.5:
    print("Vai talai Sukenas lageko xa matlab you're underweight")
elif bmi < 25:
    print("Thikai xa vai tero weight tero height heri ")
elif bmi < 30:
    print("Thikai xa vai tara ta moto vais alikati (over weight) ")
elif bmi < 35:
    print("Amama vai ta ta atti nai motais (obese) ")
else:
    print("Ta ta dharti ko boj raixas ja marna lai")