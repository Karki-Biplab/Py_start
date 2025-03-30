


#############https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=%2Fworlds%2Ftutorial_en%2Falone.json#####
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around_move():
    turn_right()
    turn_left()


# Alone
def swastik_bana():
    turn_around_move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# swastik_bana()



def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def inst_jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Hurdle1
# for pillar in range(6):
#    jump()

# Hurdle2
# while not at_goal():
#    jump()


# Hurdle3
# while not at_goal():
#    while wall_in_front():
#        inst_jump()
#        while at_goal():
#            done()
#    while not wall_in_front():
#        move()
#        while at_goal():
#            done()

# Hurdle4
# while not at_goal():
#    if right_is_clear():
#        turn_right()
#    elif wall_in_front():
#        turn_left()
#    if front_is_clear():
#        move()

def jump_walk2stepf():
    turn_left()
    move()
    turn_right()
    move()
    move()


def turn_back():
    turn_left()
    turn_left()


def ret_jump():
    turn_left()
    move()
    turn_right()
    move()
    move()

# #NewsPaper0#
#
# take()
# jump_walk2stepf()
# jump_walk2stepf()
# jump_walk2stepf()
# put()
# turn_back()
# move()
# move()
# ret_jump()
# ret_jump()
# turn_left()
# move()

# #NewsPaper1#
#
# take("star")
# jump_walk2stepf()
# jump_walk2stepf()
# jump_walk2stepf()
# take("token")
# take("token")
# take("token")
# put("star")
# turn_back()
# move()
# move()
# ret_jump()
# ret_jump()
# turn_left()
# move()