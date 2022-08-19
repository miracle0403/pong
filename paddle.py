from turtle import Turtle
import time


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(10, 2)
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        if new_y < 210:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        if new_y > -210:
            self.goto(self.xcor(), new_y)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        time.sleep(1)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bouncey(self):
        self.y_move *= -1

    def bouncex(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bouncex()


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.right = 0
        self.left = 0
        self.max = 10
        self.goto(0, 280)
        self.write(f"Left  {self.left}: {self.right} Right")

    def add_score_left(self):
        self.left += 1
        self.goto(0, 280)
        self.clear()
        self.write(f"Left  {self.left}: {self.right} Right")
        return self.left

    def add_score_right(self):
        self.right += 1
        self.goto(0, 280)
        self.clear()
        self.write(f"Left  {self.left}: {self.right} Right")
        return self.right

    def gameover(self):
        if self.right == self.max:
            self.goto(0, 0)
            self.clear()
            self.write(f"Left  {self.left}: {self.right} Right \n GAMEOVER \n Player Right Wins")

        if self.left == self.max:
            self.goto(0, 0)
            self.clear()
            self.write(f"Left  {self.left}: {self.right} Right \n GAMEOVER \n Player Left Wins")

