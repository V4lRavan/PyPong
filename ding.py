
import turtle
import winsound

window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)


#score
scoreOne=0
scoreTwo=0

#PlayerOne
playerOne = turtle.Turtle()
playerOne.speed(0)
playerOne.shape("square")
playerOne.color("red")
playerOne.shapesize(stretch_wid=5,stretch_len=1)
playerOne.penup()
playerOne.goto(-350,0)


#PlayerTwo
playerTwo = turtle.Turtle()
playerTwo.speed(0)
playerTwo.shape("square")
playerTwo.color("green")
playerTwo.shapesize(stretch_wid=5,stretch_len=1)
playerTwo.penup()
playerTwo.goto(350,0)

#Ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("blue")
ball.penup()
ball.goto(0,0)
ball.dx=0.1
ball.dy=0.1


#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 PlayerB: 0",align="center",font=("Courier",24,"normal"))


def PlayerOneUp():
  y=playerOne.ycor()
  y+=20
  playerOne.sety(y)

def PlayerOneDown():
  y=playerOne.ycor()
  y-=20
  playerOne.sety(y)
  
  
def PlayerTwoUp():
  y=playerTwo.ycor()
  y+=20
  playerTwo.sety(y)

def PlayerTwoDown():
  y=playerTwo.ycor()
  y-=20
  playerTwo.sety(y)

window.listen()
window.onkeypress(PlayerOneUp,"w")
window.onkeypress(PlayerOneDown,"s")
window.onkeypress(PlayerTwoUp,"Up")
window.onkeypress(PlayerTwoDown,"Down")

while True:
  window.update()

  ball.setx(ball.xcor()+ball.dx) 
  ball.sety(ball.ycor()+ball.dy)


  #border collision
  if ball.ycor()>290:
    ball.sety(290)
    ball.dy*=-1
    winsound.PlaySound("jump.wav",winsound.SND_ASYNC)

  if ball.ycor()<-290:
    ball.sety(-290)
    ball.dy*=-1
    winsound.PlaySound("jump.wav",winsound.SND_ASYNC)

  if ball.xcor()>390:
    ball.goto(0,0)
    ball.dx*=-1
    scoreOne+=1
    pen.clear()
    pen.write("Player A: {} PlayerB: {}".format(scoreOne,scoreTwo),align="center",font=("Courier",24,"normal"))
    winsound.PlaySound("jump.wav",winsound.SND_ASYNC)

  if ball.xcor()<-390:
    ball.goto(0,0)
    ball.dx*=-1
    scoreTwo+=1
    pen.clear()
    pen.write("Player A: {} PlayerB: {}".format(scoreOne,scoreTwo),align="center",font=("Courier",24,"normal"))
    winsound.PlaySound("jump.wav",winsound.SND_ASYNC)

  if (ball.xcor() > 340 and ball.xcor() < 350)and(ball.ycor()< playerTwo.ycor()+ 40 and ball.ycor()>playerTwo.ycor() -40):
    ball.setx(340)
    ball.dx*=-1
    winsound.PlaySound("jump.wav",winsound.SND_ASYNC)


  if (ball.xcor() < -340 and ball.xcor()> -350)and(ball.ycor()< playerOne.ycor()+ 40 and ball.ycor()>playerOne.ycor() -40):
    ball.setx(-340)
    ball.dx*=-1
    winsound.PlaySound("jump.wav",winsound.SND_ASYNC)

