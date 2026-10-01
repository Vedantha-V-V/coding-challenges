from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.tracer(0)


left_pad=Paddle(-350)
right_pad=Paddle(350)
ball=Ball()
score=Scoreboard()

screen.listen()
screen.onkey(right_pad.go_up,"Up")
screen.onkey(right_pad.go_down,"Down")
screen.onkey(left_pad.go_up,"w")
screen.onkey(left_pad.go_down,"s")

game_is_on = True
speed=0.1
loop=0
while(game_is_on):
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() <= -290:
        ball.bounce()

    #Detect with collision with right paddle
    if ball.distance(right_pad) < 50 and ball.xcor() > 330:
        ball.contact()

    #Detect the collision with left paddle
    if ball.distance(left_pad) < 50 and ball.xcor() < -330:
        ball.contact()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        time.sleep(1)

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        time.sleep(1)



screen.exitonclick()