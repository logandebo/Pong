from turtle import Turtle
from paddle import Paddle
from pong_field import BOTTOM_WALL_YCOR, TOP_WALL_YCOR

BALL_COLOR = "white"
BALL_SHAPE = "circle"

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color(BALL_COLOR)
        self.shape(BALL_SHAPE)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        # self.setheading()
        self.speed(10)

    def move(self, heading="same", distance=2):
        if heading != "same":
            self.setheading(heading)
        self.forward(distance)

    # Checks for collision with wall
    def bottom_wall_collision(self):
        if self.ycor() <= BOTTOM_WALL_YCOR + 5:
            return True

    def top_wall_collision(self):
        if self.ycor() >= TOP_WALL_YCOR - 5:
            return True

    def goal_on_left(self):
        if self.xcor() < -400:
            return True

    def goal_on_right(self):
        if self.xcor() > 400:
            return True

    def reset_ball(self):
        self.goto(x=0, y=0)