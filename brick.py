from turtle import Turtle

class Brick(Turtle):
    
    def __init__(self, position, color = "red"):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=2.5) 
        self.penup()
        self.goto(position)
    
    def break_brick(self):
        self.hideturtle()