from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from turtle import Screen
from pong_field import Field
import time


# Checks for paddle/ball collision
def ball_hits_paddle(paddle):
    global ball_moving_left
    global ball_moving_right
    if ball_moving_left:
        if paddle.bottom_segment.xcor() < ball.xcor() < paddle.bottom_segment.xcor() + 20:
            if paddle.bottom_segment.ycor() + 70 > ball.ycor() > paddle.bottom_segment.ycor() - 10:
                return True
    elif ball_moving_right:
        if paddle.bottom_segment.xcor() > ball.xcor() > paddle.bottom_segment.xcor() - 20:
            if paddle.bottom_segment.ycor() + 70 > ball.ycor() > paddle.bottom_segment.ycor() - 10:
                return True


def return_ball_direction():
    global ball_heading
    global ball_moving_right
    global ball_moving_left
    if ball_heading >= 360:
        ball_heading -= 360
    elif ball_heading < 0:
        ball_heading += 360
    if ball_heading < 90 or ball_heading > 270:
        ball_moving_right = True
        ball_moving_left = False
    elif 90 < ball_heading < 270:
        ball_moving_left = True
        ball_moving_right = False



Window_Width = 800
Window_Height = 600

screen = Screen()
screen.setup(width=Window_Width, height=Window_Height)
screen.bgcolor("black")

screen.tracer(0)

# Setting Creation
scoreboard = Scoreboard()
field = Field()
paddle_1 = Paddle(x_cor=-350)
paddle_2 = Paddle(x_cor=350)
ball = Ball()

screen.update()

screen.listen()
screen.onkey(fun=paddle_1.move_up, key="w")
screen.onkey(fun=paddle_1.move_down, key="s")
screen.onkey(fun=paddle_2.move_up, key="Up")
screen.onkey(fun=paddle_2.move_down, key="Down")


game_is_on = True
ball_moving_left = False
ball_moving_right = False

ball_heading = 200
ball.move(ball_heading)

# ball_speed =

while game_is_on:
    # time.sleep(0.0001)
    if ball.goal_on_left():
        scoreboard.p2_scores()
        ball.reset_ball()
        ball_heading += 180
    if ball.goal_on_right():
        scoreboard.p1_scores()
        ball.reset_ball()
        ball_heading += 180
    screen.update()
    return_ball_direction()
    ball.move(heading=ball_heading,distance=8)


    if ball_moving_left:

        # Checks if ball collides with left paddle
        if ball_hits_paddle(paddle_1):

            ball_heading += 180 - ball_heading * 2
            return_ball_direction()

            ball.move(heading=ball_heading, distance=3)


        # Checks if ball collides with wall
        elif ball.bottom_wall_collision():
            ball_heading -= (ball_heading - 180) * 2
            return_ball_direction()
            ball.move(heading=ball_heading, distance=3)


        elif ball.top_wall_collision():
            ball_heading += (180 - ball_heading) * 2
            return_ball_direction()
            ball.move(heading=ball_heading, distance=3)



        else:
            ball.move(ball_heading)

    if ball_moving_right:

        # Checks if ball collides with right paddle
        if ball_hits_paddle(paddle_2):

            ball_heading += 180 - ball_heading * 2
            return_ball_direction()
            ball.move(heading=ball_heading, distance=3)

        # Checks if ball collides with wall
        elif ball.bottom_wall_collision():
            ball_heading += (360 - ball_heading) * 2
            return_ball_direction()
            ball.move(heading=ball_heading, distance=3)
        elif ball.top_wall_collision():
            ball_heading -= ball_heading * 2
            return_ball_direction()
            ball.move(heading=ball_heading, distance=3)
        else:
            ball.move(ball_heading)


    # for seg in paddle_1.paddle_segments:
    #     if ball.xcor() > seg.xcor() and ball.xcor() < seg.xcor() + 20:
    #
    #         ball.move(0)
    #     else:
    #         ball.move(180)





    time.sleep(.025)









screen.exitonclick()