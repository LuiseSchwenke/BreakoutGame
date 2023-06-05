from turtle import Turtle

FONT = 'Arial', 20, 'normal'


class ScoreBoard(Turtle):

    def __init__(self, position, alignment):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.write(f"Score: {self.score}", align=alignment, font=FONT)
        self.hideturtle()

    def increase_score(self, position, alignment):
        self.score += 1
        self.clear()
        self.goto(position)
        self.write(f"Score: {self.score}", align=alignment, font=FONT)

    def reset_score(self, position, alignment):
        self.clear()
        self.score = 0
        self.goto(position)
        self.write(f"Score: {self.score}", align=alignment, font=FONT)

    def winner(self, position):
        self.clear()
        self.goto(position)
        self.write("Congrats, You won!", font=FONT)
        self.score = 0





