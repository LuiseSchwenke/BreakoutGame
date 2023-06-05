from turtle import Turtle


STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = STARTING_MOVE_DISTANCE

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def change_y_direction(self):
        self.y_move *= -1

    def change_x_direction(self):
        self.x_move *= -1

    def reset_ball(self):
        self.home()

    def speed_up(self):
        self.ball_speed += MOVE_INCREMENT
