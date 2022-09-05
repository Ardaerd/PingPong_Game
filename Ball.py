import turtle

class Ball:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ball()
    
    def ball(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(self.x, self.y)   
        self.ball.dx = 0.15 
        self.ball.dy = 0.15 