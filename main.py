from turtle import Turtle, Screen
from paddle import Paddle

paddle = Paddle()
screen = Screen()

screen.title("Hit the damn ball!!!")
screen.setup(800, 600)
screen.bgcolor("black")


screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")
screen.onkeypress(paddle.up, "Up")
screen.onkeypress(paddle.down, "Down")

screen.exitonclick()
