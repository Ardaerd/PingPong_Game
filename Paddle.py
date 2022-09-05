import turtle

class Paddle:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.paddle()

    # initializing the paddle
    def paddle(self):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid = 5, stretch_len = 1)
        self.paddle.penup()
        self.paddle.goto(self.x, self.y)
        
    # Method for going up
    def paddle_up(self):
        y = self.paddle.ycor()
        y += 20
        self.paddle.sety(y)
        
    # Method for going down
    def paddle_down(self):
        y = self.paddle.ycor()
        y -= 20
        self.paddle.sety(y)