############    DAY 4       #############

#now making sissor paper and rock after completing all exersises#
rock = '''
    ___
---'   __)
      (___)
      (___)
      (__)
---._(__)
'''

paper = '''
    ___
---'   ___)_
          ____)
          _____)
         _____)
---.______)
'''

scissors = '''
    ____
---'   __)_____
          ______)
       __________)
      (___)
---._(___)
'''

act_list = [ rock, paper, scissors]
hum_cho = int(input("What you wanna choose? Rock(0), Paper(1), Scissors(2)  --> "))
hum_choice = act_list[hum_cho]
print(f" You Choose {hum_choice}")

com_cho =