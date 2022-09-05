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
        self.ball.color("yellow")
        self.ball.penup()
        self.ball.goto(self.x, self.y)   
        self.ball.dx = 6 
        self.ball.dy = 6 
        
    # Set the coordinates of the ball
    def setCoordinates(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)
        
        
    # Checking Y coordinate
    def checkBorder_Y(self,limit):
        if limit < 0 and self.ball.ycor() < limit:
            self.ball.sety(limit)   
            self.ball.dy *= -1
        
        if limit > 0 and self.ball.ycor() > limit:
            self.ball.sety(limit)   
            self.ball.dy *= -1
            
            
    # Checking X coordinate
    def checkBorder_X(self,limit):
        if self.ball.xcor() < -limit:
            self.ball.goto(0,0)
            self.ball.dx *= -1
        
        elif self.ball.xcor() > limit:
            self.ball.goto(0,0)
            self.ball.dx *= -1
        
    def clearBall(self):
        self.ball.clear()
