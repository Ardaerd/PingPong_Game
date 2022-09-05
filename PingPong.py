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
ball_1 = Ball(0,0)

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
    ball_1.setCoordinates()
    
    # Border Checking
    ball_1.checkBorder_Y(290)
    ball_1.checkBorder_Y(-290)

    ball_1.checkBorder_X(390)
    
    # Paddle and ball collision 
    # For paddle_b
    if (ball_1.ball.xcor() > 340 and ball_1.ball.xcor() < 350) and (ball_1.ball.ycor() < paddle_b.paddle.ycor() + 40 and ball_1.ball.ycor() > paddle_b.paddle.ycor() - 40):
        ball_1.ball.setx(340)
        ball_1.ball.dx *= -1

    # For paddle_a
    if (ball_1.ball.xcor() < -340 and ball_1.ball.xcor() > -350) and (ball_1.ball.ycor() < paddle_a.paddle.ycor() + 40 and ball_1.ball.ycor() > paddle_a.paddle.ycor() - 40):
        ball_1.ball.setx(-340)
        ball_1.ball.dx *= -1
