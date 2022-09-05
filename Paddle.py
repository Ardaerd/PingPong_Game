import turtle

class Paddle:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.paddle()

    def paddle(self):
        paddle = turtle.Turtle()
        paddle.speed(0)
        paddle.shape("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid = 5, stretch_len = 1)
        paddle.penup()
        paddle.goto(self.x, self.y)