import chest
import levels
import turtle
import player as player_class


WIDTH = 1000
HEIGHT = 700

win = turtle.Screen()
win.title("Dungeon")
win.setup(WIDTH, HEIGHT)
win.bgcolor("black")


current_dungeon = levels.Dungeon(levels.LEVEL_1, "white")    # load dungeon
current_dungeon.draw()

player = player_class.Player()

turtle.listen()
turtle.onkey(player.go_up,"z")
turtle.onkey(player.go_down,"s")
turtle.onkey(player.go_left,"q")
turtle.onkey(player.go_right,"d")

# player.move(arg)
win.mainloop()
