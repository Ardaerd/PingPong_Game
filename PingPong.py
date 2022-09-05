import time
import turtle
from Paddle import Paddle
from Ball import Ball
from Pen import Pen
import winsound
from timeit import default_timer as timer
        
screen = turtle.Screen()
screen.title("PingPong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
turtle.delay(0)
# Create listener for the key pressings
screen.listen()

# list of the balls
balls = []

# Create paddle A
paddle_a = Paddle(-350,0)

# Create paddle B
paddle_b = Paddle(350,0)

# Create Ball
ball_1 = Ball(0,0)
balls.append(ball_1)

# Create the scoreBoard
pen = Pen()

# For Paddle which is going up
screen.onkeypress(paddle_a.paddle_up,"w")
screen.onkeypress(paddle_b.paddle_up,"Up")


# For Paddle which is going down
screen.onkeypress(paddle_a.paddle_down,"s")
screen.onkeypress(paddle_b.paddle_down,"Down")

def collision(limit):
    
    for ball in balls:
      # For paddle_b
        if (ball.ball.xcor() > limit and ball.ball.xcor() < limit + 10) and (ball.ball.ycor() < paddle_b.paddle.ycor() + 45 and ball.ball.ycor() > paddle_b.paddle.ycor() - 45):
            ball.ball.setx(limit)
            ball.ball.dx *= -1

        # For paddle_a
        if (ball.ball.xcor() < -limit and ball.ball.xcor() > -limit -10) and (ball.ball.ycor() < paddle_a.paddle.ycor() + 45 and ball.ball.ycor() > paddle_a.paddle.ycor() - 45):
            ball.ball.setx(-limit)
            ball.ball.dx *= -1

start = timer()

# Main game loop
while True:
    time.sleep(1 / 60)
    screen.update()
    
    for ball in balls:
        # Move the ball
        ball.setCoordinates()
    
        # Border Checking
        ball.checkBorder_Y(290)
        ball.checkBorder_Y(-290)
        ball.checkBorder_X(390)

    
        # Updating the score board
        if ball.ball.xcor() <= -390:
            pen.score_b += 1
            pen.pen.clear()
            pen.scoreBoard()
            winsound.PlaySound("PingPong\giddylaugh.wav", winsound.SND_ASYNC)
            if len(balls) > 1:
                if type(ball) is Ball:
                    ball.clearBall()
                balls.remove(ball)
            start = timer()
        
        elif ball.ball.xcor() >= 390:
            pen.score_a += 1
            pen.pen.clear()
            pen.scoreBoard()
            winsound.PlaySound("PingPong\giddylaugh.wav", winsound.SND_ASYNC)
            start = timer()
            if len(balls) > 1:
                if type(ball) is Ball:
                    ball.clearBall()
                balls.remove(ball)
            start = timer()


    # Paddle and ball collision 
    collision(340)
    
    end = timer()
    
    if (end - start) > 5:
        start = timer()
        new_ball = Ball(0,0)
        balls.append(new_ball)
