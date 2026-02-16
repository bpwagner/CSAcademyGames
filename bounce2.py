#bounce2
#Brian Wagner 2026
#www.codewithmrwagner.com
#This code works in the Sandbox area
#of CS Academy https://academy.cs.cmu.edu/


#below are variables
x=10
y=200
dx = 6
dy = 5

#set the background and the ball
app.background = 'white'
ball = Circle(x,y,20, fill = 'red')

#new code
paddle = Rect(200,360,80,20, fill = 'blue')

#onStep() moves the ball
def onStep():
    global dx
    global dy
    
    #newcode
    #this code checks to see if paddle hits the ball
    if paddle.hitsShape(ball):
        dy = dy * -1  #bounce the ball
    
    ball.centerX += dx
    ball.centerY += dy
    
    if ball.centerX > 400 or ball.centerX < 0:
        dx = dx * -1
    if ball.centerY >400 or ball.centerY < 0:
        dy = dy * -1
        
    pass

#new code
def onMouseMove(mouseX, mouseY):
    paddle.centerX = mouseX
    pass
