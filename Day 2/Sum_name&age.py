#########DAY 2##########

name = input("What is your name? ")
age = input("What is your age? ")
sumname = str(len(name))
sumage = str(age)
print("Your name has " + sumname + " letters and your age is " + age)
prname = int(sumname[0]) + int(sumname[1])
prage = int(sumage[0]) + int(sumage[1])
# print("the sum of your name total letters and age is " int(prname[0]) + int(prage[0]))
sum = prname + prage
print("the sum of your name total letters and age is " + str(sum))
