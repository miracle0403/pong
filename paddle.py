from turtle import Turtle
import time

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(10, 2)
        self.goto(350, 0)

    def up(self):
        new_y = self.ycor() + 20
        if new_y < 210:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        if new_y > -210:
            self.goto(self.xcor(), new_y)
