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

player = Player()

turtle.listen()
turtle.onkey(player.go_up,"z")
turtle.onkey(player.go_down,"s")
turtle.onkey(player.go_left,"q")
turtle.onkey(player.go_right,"d")

# player.move(arg)
win.mainloop()
