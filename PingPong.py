import time
import turtle
from Paddle import Paddle
from Ball import Ball
from Pen import Pen
import winsound
        
screen = turtle.Screen()
screen.title("PingPong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
turtle.delay(0)
# Create listener for the key pressings
screen.listen()

# Create paddle A
paddle_a = Paddle(-350,0)

# Create paddle B
paddle_b = Paddle(350,0)

# Create Ball
ball_1 = Ball(0,0)

# Create the scoreBoard
pen = Pen()

# For Paddle which is going up
screen.onkeypress(paddle_a.paddle_up,"w")
screen.onkeypress(paddle_b.paddle_up,"Up")


# For Paddle which is going down
screen.onkeypress(paddle_a.paddle_down,"s")
screen.onkeypress(paddle_b.paddle_down,"Down")

def collision(limit):
      # For paddle_b
    if (ball_1.ball.xcor() > limit and ball_1.ball.xcor() < limit + 10) and (ball_1.ball.ycor() < paddle_b.paddle.ycor() + 45 and ball_1.ball.ycor() > paddle_b.paddle.ycor() - 45):
        ball_1.ball.setx(limit)
        ball_1.ball.dx *= -1

    # For paddle_a
    if (ball_1.ball.xcor() < -limit and ball_1.ball.xcor() > -limit -10) and (ball_1.ball.ycor() < paddle_a.paddle.ycor() + 45 and ball_1.ball.ycor() > paddle_a.paddle.ycor() - 45):
        ball_1.ball.setx(-limit)
        ball_1.ball.dx *= -1

# Main game loop
while True:
    time.sleep(1 / 60)
    screen.update()
    
    # Move the ball
    ball_1.setCoordinates()
    
    # Border Checking
    ball_1.checkBorder_Y(290)
    ball_1.checkBorder_Y(-290)
    ball_1.checkBorder_X(390)

    
    # Updating the score board
    if ball_1.ball.xcor() <= -390:
        pen.score_b += 1
        pen.pen.clear()
        pen.scoreBoard()
        winsound.PlaySound("PingPong\giddylaugh.wav", winsound.SND_ASYNC)
        
    elif ball_1.ball.xcor() >= 390:
        pen.score_a += 1
        pen.pen.clear()
        pen.scoreBoard()
        winsound.PlaySound("PingPong\giddylaugh.wav", winsound.SND_ASYNC)

    # Paddle and ball collision 
    collision(340)
