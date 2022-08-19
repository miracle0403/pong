import time
from turtle import Turtle, Screen
from paddle import Paddle, Ball, ScoreBoard


gameon = True


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

screen = Screen()
winning_score = 10

screen.title("Hit the damn ball!!!")
screen.setup(800, 600)
screen.bgcolor("black")

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

speed = 0.1
while gameon:
    time.sleep(speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncey()

    # detect collision with the paddle
    if ball.distance(r_paddle) < 100 and ball.xcor() > 320 or ball.distance(l_paddle) < 100 and ball.xcor() < -320:
        speed -= 0.009
        time.sleep(speed)
        ball.bouncex()

    if ball.xcor() > 380:
        ball.reset_position()
        time.sleep(0.1)
        sc = score.add_score_left()
        if sc == winning_score:
            gameon = False

    if ball.xcor() < -380:
        ball.reset_position()
        time.sleep(0.1)
        sc = score.add_score_right()
        if sc == winning_score:
            gameon = False


screen.exitonclick()
