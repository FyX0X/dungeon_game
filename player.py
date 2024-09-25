import turtle

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        
        #if (move_to_x, move_to_y) not in walls:
        self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        
        #if (move_to_x, move_to_y) not in walls:
        self.goto(move_to_x, move_to_y)
            
    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        
        #if (move_to_x, move_to_y) not in walls:
        self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        
        #if (move_to_x, move_to_y) not in walls:
        self.goto(move_to_x, move_to_y)

player = Player()

#Keyboard bindings
turtle.listen()
turtle.onkey(player.go_up,"z")
turtle.onkey(player.go_down,"s")
turtle.onkey(player.go_left,"q")
turtle.onkey(player.go_right,"d")
        
