import turtle
from Paddle import Paddle
from Ball import Ball
        
screen = turtle.Screen()
screen.title("PingPong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
# Create listener for the key pressings
screen.listen()

# Create paddle A
paddle_a = Paddle(-350,0)

# Create paddle B
paddle_b = Paddle(350,0)

# Create Ball
ball = Ball(0,0)

# For Paddle which is going up
screen.onkeypress(paddle_a.paddle_up,"w")
screen.onkeypress(paddle_b.paddle_up,"Up")


# For Paddle which is going down
screen.onkeypress(paddle_a.paddle_down,"s")
screen.onkeypress(paddle_b.paddle_down,"Down")


# Main game loop
while True:
    screen.update()
    
    # Move the ball
    ball.ball.setx(ball.ball.xcor() + ball.ball.dx)
    ball.ball.sety(ball.ball.ycor() + ball.ball.dy)

