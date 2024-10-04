import chest
import levels
import turtle
import player as player_class
import dungeon_generator


WIDTH = 1000
HEIGHT = 655

win = turtle.Screen()
win.title("Dungeon")
win.setup(WIDTH, HEIGHT)
win.bgcolor("black")

dungeon_maker = dungeon_generator.DungeonGenerator()
generated_level = dungeon_maker.create_dungeon(25)
current_dungeon = levels.Dungeon(generated_level, "white")    # load dungeon

# current_dungeon = levels.Dungeon(levels.LEVEL_1, "white")    # load dungeon
current_dungeon.draw()

player = current_dungeon.player

turtle.listen()
turtle.onkey(player.go_up, "z")
turtle.onkey(player.go_down, "s")
turtle.onkey(player.go_left, "q")
turtle.onkey(player.go_right, "d")

# player.move(arg)
win.mainloop()
