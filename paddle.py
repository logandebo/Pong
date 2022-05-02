from turtle import Turtle
from pong_field import BOTTOM_WALL_YCOR, TOP_WALL_YCOR


class Paddle(Turtle):

    def __init__(self,x_cor):
        super().__init__()
        paddle_xcor = x_cor
        self.paddle_segments = []
        self.create_paddle(paddle_xcor)
        self.bottom_segment = self.paddle_segments[0]

    def create_paddle(self, paddle_xcor):
        for segment in range(4):
            new_seg = Turtle()
            new_seg.color("white")
            new_seg.shape("square")
            new_seg.turtlesize(1, 1)
            new_seg.penup()
            self.paddle_segments.append(new_seg)
        y_cor = -20
        for seg in range(4):
            self.paddle_segments[seg].goto(x=paddle_xcor, y=y_cor)
            y_cor += 20

    def move_up(self):
        if not self.paddle_on_top_edge():
            for seg in self.paddle_segments:
                seg.setheading(90)
                seg.forward(20)

    def move_down(self):
        if not self.paddle_on_bot_edge():
            for seg in self.paddle_segments:
                seg.setheading(270)
                seg.forward(20)

    def paddle_on_bot_edge(self):
        if self.bottom_segment.ycor() - BOTTOM_WALL_YCOR < 25:
            return True

    def paddle_on_top_edge(self):
        if TOP_WALL_YCOR - self.bottom_segment.ycor() < 85:
            return True
