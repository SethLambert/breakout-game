from turtle import Turtle

class TextDisplay(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        
    def update_text(self, message, color):
        self.clear()
        self.goto(0,0)
        self.color(color)
        self.write(message, align="center", font=("Courier", 16, "normal"))
