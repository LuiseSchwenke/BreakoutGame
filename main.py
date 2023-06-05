from turtle import Screen
from paddle import MovingPaddle
from ball import Ball
from bricks import Bricks
import time
from score import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Breakout Game")
screen.tracer(0)
ball = Ball()
ball.speed(10)
bricks = Bricks()

paddle = MovingPaddle((0, -270))
score = ScoreBoard((150, 280), "right")

screen.listen()
screen.onkeypress(paddle.paddle_right, "Right")
screen.onkeypress(paddle.paddle_left, "Left")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    for brick in bricks.bricks:
        length = len(bricks.bricks)
        if ball.distance(brick) < 40:
            brick.quantity -= 1
            ball.change_y_direction()
            if brick.quantity == 0:
                brick.clear()
                brick.goto(3000, 3000)
                bricks.bricks.remove(brick)
                score.increase_score((150, 230), "right")
        if length == 0:
            score.winner((-370, 0))
            time.sleep(3)
            screen.bye()

    if ball.ycor() > 260:
        ball.change_y_direction()

    if ball.ycor() < -270:
        ball.reset_ball()
        score.reset_score((150, 230), "right")
        bricks.create_all_lanes()
        time.sleep(1)

    if ball.distance(paddle) < 40 and ball.ycor() < 350:
        ball.speed_up()
        ball.change_y_direction()

    if ball.xcor() > 370 or ball.xcor() < -370:
        ball.change_x_direction()

screen.exitonclick()
