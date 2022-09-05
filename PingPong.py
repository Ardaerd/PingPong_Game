import turtle
from Paddle import Paddle
from Ball import Ball
        
screen = turtle.Screen()
screen.title("PingPong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create paddle A
paddle_a = Paddle(-350,0)

# Create paddle B
paddle_b = Paddle(350,0)

# Create Ball
ball = Ball(0,0)

# Main game loop
while True:
    screen.update()

