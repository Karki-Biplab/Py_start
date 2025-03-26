#################### Day 3 (IF/ELSE/Nested) ###################

print("Khazana Ko Tapu Ma Tapai Lai Swagatam ")
print("Tailey Khazana Vettauna parxa aba ")
task1 = input("              right Janxas Ki left? -->")
if task1 == "left":
    task2 = input("              Badhai xa euta kattyo aba van swim garxas ki wait garxas? -->")
    if task2 == "wait":
        task3 = input("Khusi lagyo taile wait garis. Aba van Kun Dhoka xirxas?   green/red/blue/yellow/purple/.....etc -->")
        if task3 =="yellow":
            print("Jitis Taileyyy Khusi Mana ja ")
        elif task3 == "red":
            print("Ta Dadera Maris Aago ra Petrol le hahahhaha GameOver Mr.Kharani")

        elif task3 == "blue":
            print("Talai Rakxyes le Khayo..  GameOver Rakhxes ko Guuuu ")

        else:
            print("Ja ta maris. GameOver")

    else:
        print("Attacked by trout.  Game Over ")


else:
    print("################GameOver###################")

#i asked chatgpt to make it spicer

###########ChatGPT Version#########################
# print("🌴💰 Khazana Ko Tapu Ma Tapai Lai Swagatam! 💰🌴")
# print("Tailey Khazana Vettauna parxa aba... 😈")
#
# task1 = input("👉 Right Janxas Ki Left? (right/left) --> ").lower()
#
# if task1 == "left":
#     task2 = input("🚣‍♂️ Badhai xa! Euta kattis aba, van swim garxas ki wait garxas? (swim/wait) --> ").lower()
#
#     if task2 == "wait":
#         task3 = input(
#             "🔑 Khusi lagyo, tailey wait garis. Aba van, Kun Dhoka xirxas? (green/red/blue/yellow/purple) --> ").lower()
#
#         if task3 == "yellow":
#             print("🎉 **JITISSS!** Tailey Khazana Vettyas. Aba **party time**! 🍾🎊")
#         elif task3 == "red":
#             print("🔥 **Ta Dadera Maris!** Aago ra Petrol le... Hahaha **Game Over Mr. Kharani!** 😂")
#         elif task3 == "blue":
#             print("🐍 **Talai Rakxes le Khayo!** Jindagi bhari guu banera basne vaixas... **Game Over!** 🤢")
#         elif task3 == "purple":
#             print("👻 **Taile Bhoot Ko Kotha Khulyas!** Aba timro atma ni bhatkkidaina... 😱 **Game Over!**")
#         else:
#             print("💀 **Galat Dhoka Xiryas!** Aba tailey ta narak ko ticket kati halis! **Game Over!** 🚪👹")
#
#     else:
#         print("🐟 **Tailey Swim Garna Khojis!** Trout le chabaayechas... **Game Over!** 😂")
#
# else:
#     print("💀 **Ta Right Gais!** Ani tailey khutrukk parera khaai halis. **Game Over!** 😂😂😂")