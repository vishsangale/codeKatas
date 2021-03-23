def can_cross(river, speed):
    if speed >= len(river):
        return True
    change_speed = False
    if len(river) == 1 and speed > 1:
        return True
    if len(river) > speed and river[speed] == " ":
        change_speed = True
    print river[speed + 1]
    if change_speed and river[speed + 1] == "*":
        speed += 1
    elif change_speed and speed - 1 >= 0 and river[speed - 1] == "*" and speed > 1:
        speed -= 1
    elif not change_speed:
        speed += 1
    else:
        return False

    return can_cross(river[speed:], speed)


river1 = "*****  *   * * *  *  *  "
river2 = "** *"
river3 = "*  *"
river4 = "* *"
print can_cross(river1, 0)
