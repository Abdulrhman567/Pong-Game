from turtle import Turtle


class Bar(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.shape("square")
        self.color("orange")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(positions)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
