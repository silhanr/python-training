def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    i = 0
    while wall_on_right():
        if front_is_clear():
            move()
            i += 1
    turn_right()
    move()
    turn_right()
    while i > 0:
        move()
        i -= 1
    turn_left()


while not at_goal():
    if wall_in_front():
        turn_left()
        jump()
    else:
        move()










