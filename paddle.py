from turtle import Turtle


class MovingPaddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def paddle_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def paddle_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
