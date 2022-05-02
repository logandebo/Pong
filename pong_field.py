from turtle import Turtle

SCREEN_COLOR = "black"
FIELD_COLOR = "white"
CENTER_LINE_BASE_YCOR = -225
BOTTOM_WALL_YCOR = -250
TOP_WALL_YCOR = 250

#Playing field is 800(width)x500(height)

class Field(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.draw_center()
        self.draw_walls()

    def draw_center(self):
        self.goto(x=0, y=CENTER_LINE_BASE_YCOR)
        self.setheading(90)
        self.pendown()
        for line in range(12):
            self.pencolor(FIELD_COLOR)
            self.forward(20)
            self.pencolor(SCREEN_COLOR)
            self.forward(20)
        self.penup()
        self.color(FIELD_COLOR)

    def draw_walls(self):
        self.penup()
        self.goto(x=-400, y=BOTTOM_WALL_YCOR)
        self.pencolor("white")
        self.pendown()
        self.setheading(0)
        self.forward(800)
        self.penup()
        self.goto(x=-400, y=TOP_WALL_YCOR)
        self.pendown()
        self.setheading(0)
        self.forward(800)
        self.penup()
