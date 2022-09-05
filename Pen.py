import turtle


class Pen:

    def __init__(self):
        self.score_a = 0
        self.score_b = 0
        self.separator()
        self.scoreBoard()
        

    def separator(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        
        for x in range(-280,280,70):
            self.pen.goto(0, x)
            self.pen.write("|", align="center", font=("courier",30,"bold"))


    
    def scoreBoard(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        
        # For paddle_a
        self.pen.color("green")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(-200, 220)
        self.pen.write(f"{self.score_a}", align="center", font=("courier",50,"bold"))
        
        # For paddle_b
        self.pen.color("red")
        self.pen.goto(200, 220)
        self.pen.write(f"{self.score_b}", align="center", font=("courier",50,"bold"))
