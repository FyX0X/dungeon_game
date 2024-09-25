import turtle


LEVEL_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXP   XXXX       XXXXX X",
    "XXX    XXXX  XX   XXXXX X",
    "XXX   XXXXXXXXX   XXX   X",
    "XXX                    XX",
    "XXXXXXXXXX     XXXXX  CXX",
    "XXXXXXXXX    XXXXXXX   XX",
    "XXXXXXXXX   XX     X   XX",
    "XX   XXXX   XX     X   XX",
    "XX  XXXXX  XXX         XX",
    "XX  XXXXX  XXXXXXXXXXXXXX",
    "XX                 XXXXXX",
    "XXXXXXXXXXXXXX         XX",
    "XXX  XXXXXXXXX  X  XXX XX",
    "XXX        XXX  X  XXX XX",
    "XXXXXX     XXX  X  XXX XX",
    "XXXXXX             XXX XX",
    "XXXXXXXXXXXX  XXXXXXXX XX",
    "XXXXXX        XXXXXXXX XX",
    "XX            XXXXXXXX XX",
    "XX XXX        XXXXXXXX XX",
    "XX XXX                 XX",
    "XX XXXXXXX XXXXXXXXXXXXXX",
    "XX         XXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]


class Dungeon:
    def __init__(self, level, color="white"):
        self.level = level
        self.turtle = turtle.Turtle(shape="square", visible=True)
        self.turtle.color(color)
        self.turtle.speed(0)
        self.turtle.penup()

    def draw(self):
        """
        self.wall_turtle.penup()
        self.wall_turtle.color(self.color)"""
        self.turtle.speed(0)
        for y in range(len(self.level)):
            for x in range(len(self.level[y])):
                if self.level[y][x] == "X":
                    # calculate screen coord:
                    screen_x = -288 + 24*x
                    screen_y = 376 - 24*y
                    self.turtle.goto(screen_x, screen_y)
                    self.turtle.stamp()

