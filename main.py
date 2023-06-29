from turtle import Screen
from ball import Ball
from brick import Brick
from paddle import Paddle
import time
from level_setup import levels
from text_display import TextDisplay

screen = Screen()
screen.bgcolor("black")
screen.setup(width=400, height=600)
screen.title("Bricked Up")
screen.tracer(0)

paddle = Paddle((0,-260))
ball = Ball()
text_display = TextDisplay()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_is_on = True

level = 1
bricks = []
for i in range(len(levels[f'{level}']['positions'])):
    brick = Brick(levels[f'{level}']['positions'][i], levels[f'{level}']['colors'][i])
    bricks.append(brick)

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #detect collision with top wall
    if ball.ycor() > 280:
        #bounce ball
        ball.bounce_y()
        
    #detect collision with side wals
    if ball.xcor() > 180:
        ball.bounce_x()
        
    if ball.xcor() < -180:
        ball.bounce_x()
                
    #detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() > -260:
        ball.bounce_y()
    
    if len(bricks) == 0:
        text_display.update_text(f"Level {level} Complete!", 'white')    
        screen.update()
        game_is_on = False
    else:
        for brick in bricks:
            if ball.distance(brick) < 30:
                brick.break_brick()
                ball.bounce_y()
                bricks.remove(brick)
            
    if ball.ycor() < -300:
        text_display.update_text("Game Over", 'red')
        screen.update()
        game_is_on = False
        


screen.exitonclick()
