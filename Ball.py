import turtle

class Ball:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ball()
    
    def ball(self):
        ball = turtle.Turtle()
        ball.speed(0)
        ball.shape("square")
        ball.color("white")
        ball.penup()
        ball.goto(self.x, self.y)    