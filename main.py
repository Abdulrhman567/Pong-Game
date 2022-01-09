from turtle import Screen
from user_bar import Bar
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_bar = Bar((370, 0))
l_bar = Bar((-370, 0))
ball = Ball()
r_score = ScoreBoard((300, 260), "right")
l_score = ScoreBoard((-300, 260), "left")

screen.listen()
screen.onkey(fun=r_bar.move_up, key="Up")
screen.onkey(fun=r_bar.move_down, key="Down")
screen.onkey(fun=l_bar.move_up, key="w")
screen.onkey(fun=l_bar.move_down, key="s")

speed_num = 1
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move_ball_randomly()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_bar) < 50 and ball.xcor() > 340 or ball.distance(l_bar) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        r_score.increase_score("right")

    if ball.xcor() < -380:
        ball.reset_position()
        l_score.increase_score("left")


screen.exitonclick()
