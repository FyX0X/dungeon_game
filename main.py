import chest
import levels
import turtle
# import player

WIDTH, HEIGHT = (600, 600)

win = turtle.Screen()
win.title("Dungeon")
win.setworldcoordinates(0, HEIGHT, WIDTH, 0)        # create window of size (WIDTH, HEIGHT) with (0, 0) on top left


current_level = levels.level_1

run = True
while run:
    pass
    #player.move(arg)
    # win.mainloop