from turtle import Turtle
FONT = ("Courier", 25, "normal")


class ScoreBoard(Turtle):
    def __init__(self, position, align):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.show_scoreboard(align)

    def show_scoreboard(self, align):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=align, font=FONT)

    def increase_score(self, align):
        self.score += 1
        self.show_scoreboard(align)



