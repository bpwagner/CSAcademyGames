#bounce3
#Brian Wagner 2026
#www.codewithmrwagner.com
#This code works in the Sandbox area
#of CS Academy https://academy.cs.cmu.edu/


#below are variables
x=10
y=200
dx = 6
dy = 5

#newcode
score = 0

#set the background and the ball
app.background = 'white'
ball = Circle(x,y,20, fill = 'red')

paddle = Rect(200,360,80,20, fill = 'blue')

#newcode
myScore = Label(score, 350, 20 , size=18)

#onStep() moves the ball
def onStep():
    global dx
    global dy
    #newcode
    global score
    
    #this code checks to see if paddle hits the ball
    if paddle.hitsShape(ball):
        dy = dy * -1  #bounce the ball
        #newcode
        score = score +1
        
    
    ball.centerX += dx
    ball.centerY += dy
    
    if ball.centerX > 400 or ball.centerX < 0:
        dx = dx * -1
    if ball.centerY >400 or ball.centerY < 0:
        dy = dy * -1
        
    #newcode
    if ball.bottom >400:
        score = 0 #reset the score
        
    myScore.value = score
        
    pass

def onMouseMove(mouseX, mouseY):
    paddle.centerX = mouseX
    pass

    
