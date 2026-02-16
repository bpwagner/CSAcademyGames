#pong
#Brian Wagner 2026
#www.codewithmrwagner.com
#This code works in the Sandbox area
#of CS Academy https://academy.cs.cmu.edu/


x=200
y=200
dx = 6
dy = 5

rScore = 0
lScore = 0

#set the background and the ball
app.background = 'white'
ball = Circle(x,y,10, fill = 'red')
app.stepsPerSecond = 60 #change this to speed up or slow the ball down

#define the objects
rPaddle = Rect(20,200,20,80, fill = 'green')
lPaddle = Rect(360,200,20,80, fill = 'blue')

rScoreboard = Label(0, 50, 20 , size=18)
lScoreboard = Label(0, 350, 20 , size=18)


def onStep():  #onStep() moves the ball
    global dx
    global dy
    global rScore
    global lScore
    
    #this code checks to see if paddles hits the ball
    if rPaddle.hitsShape(ball):
        dx = dx * -1  #bounce the ball
    if lPaddle.hitsShape(ball):
        dx = dx * -1   
        
    ball.centerX = ball.centerX + dx
    ball.centerY = ball.centerY + dy
    
    if ball.centerX > 400:
        dx = dx * -1
        rScore = rScore + 1
        
    if ball.centerX < 0:
        dx = dx * -1
        lScore = lScore + 1
        
    if ball.centerY >400 or ball.centerY < 0:
        dy = dy * -1
        
    rScoreboard.value = rScore
    lScoreboard.value = lScore
    pass

def onKeyHold(keys):
    if ('a' in keys):
        rPaddle.centerY = rPaddle.centerY - 10
    if ('z' in keys):
        rPaddle.centerY = rPaddle.centerY + 10
    if ('up' in keys):
        lPaddle.centerY = lPaddle.centerY - 10
    if ('down' in keys):
        lPaddle.centerY = lPaddle.centerY + 10
    pass


    
