#at_goal()
#front_is_clear()
#right_is_clear()
#wall_in_front()
#wall_on_right()
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    while front_is_clear():
        move()
        if right_is_clear():
            if at_goal():
                break
            turn_right()
    while wall_in_front():
        if wall_on_right():
            turn_left()
        else:
            turn_right()
################################################################
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
################################################################
