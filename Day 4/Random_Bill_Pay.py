#############    DAY 4       #############

import random
names = input("Give me everybody's names seperated by comma. --> ")
splt_name = names.split(",")
num_name = len(splt_name)
py_prsn = random.randint(0,num_name-1)
pay_person = splt_name[py_prsn]
print(f" If you are in total {num_name} persons so let {pay_person} pay the whole bill....")