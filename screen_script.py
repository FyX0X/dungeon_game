import turtle


def calculate_screen_x(world_x: int):
    screen_x = -464 + 24*world_x
    return screen_x


def calculate_screen_y(world_y: int):
    screen_y = 288 - 24*world_y
    return screen_y
