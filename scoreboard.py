from turtle import Turtle

SCOREBOARD_COLOR = "white"
SCREEN_COLOR = "black"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.color(SCOREBOARD_COLOR)
        self.p1_score = 0
        self.p2_score = 0
        self.draw_score()

    def draw_score(self):
        self.goto(x=-50, y=240)
        self.write(arg=f"{self.p1_score}", align="center", font=("Courier", 40, "normal"))
        self.goto(x=50, y=240)
        self.write(arg=f"{self.p2_score}", align="center", font=("Courier", 40, "normal"))

    def p1_scores(self):
        self.p1_score += 1
        self.clear()
        self.draw_score()

    def p2_scores(self):
        self.p2_score += 1
        self.clear()
        self.draw_score()


