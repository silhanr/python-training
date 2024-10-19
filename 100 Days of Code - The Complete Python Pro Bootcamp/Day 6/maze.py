def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if wall_in_front():
        if wall_on_right():
            turn_left()
        else:
            turn_right()

    else:
        move()