import turtle
import screen_script

class Player(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

        self.x = x
        self.y = y
        self.move_to_world(x, y)

    def move_to_world(self, world_x, world_y):
        self.x = world_x
        self.y = world_y
        screen_x = screen_script.calculate_screen_x(world_x)
        screen_y = screen_script.calculate_screen_y(world_y)
        print(self.x, "\t", self.y)
        
        self.goto(screen_x, screen_y)




    def go_up(self):
        move_to_world_x = self.x
        move_to_world_y = self.y - 1
        
        #if (move_to_world_x, move_to_world_y) not in walls:
        self.move_to_world(move_to_world_x, move_to_world_y)

    def go_down(self):
        move_to_world_x = self.x
        move_to_world_y = self.y + 1
        
        #if (move_to_world_x, move_to_world_y) not in walls:
        self.move_to_world(move_to_world_x, move_to_world_y)
            
    def go_left(self):
        move_to_world_x = self.x - 1
        move_to_world_y = self.y
        
        #if (move_to_world_x, move_to_world_y) not in walls:
        self.move_to_world(move_to_world_x, move_to_world_y)

    def go_right(self):
        move_to_world_x = self.x + 1
        move_to_world_y = self.y
        
        #if (move_to_world_x, move_to_world_y) not in walls:
        self.move_to_world(move_to_world_x, move_to_world_y)
        