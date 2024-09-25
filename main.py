import chest
import levels
import turtle
import player


WIDTH = 700
HEIGHT = 800

win = turtle.Screen()
win.title("Dungeon")
win.setup(WIDTH, HEIGHT)
win.bgcolor("black")


current_dungeon = levels.Dungeon(levels.LEVEL_1, "white")    # load dungeon
current_dungeon.draw()

win.listen()


# player.move(arg)
win.mainloop()
