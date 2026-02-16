#Flappy
#Brian Wagner 2026
#www.codewithmrwagner.com
#This code works in the Sandbox area
#of CS Academy https://academy.cs.cmu.edu/


import random  #ability for random numbers
app.background = 'lightCyan'
ground = Rect(0,300,400,100, fill = gradient('tan','wheat',start='top'))
  
#make shape and score board
bird = Oval(100,200,20,40, fill = 'yellow', border='green', borderWidth=1)
bird.rotateAngle = 90

#make 5 blocks
topPipes = []
bottomPipes = []
for i in range(4):
    x = 600 + (i * 300)
    y = random.randint(-400,-100)
    by = y + 400 + 100
    topPipes.append( Rect(x, y, 60, 400, fill = 'limeGreen', border='black', borderWidth=1))
    bottomPipes.append( Rect(x, by, 60, 400, fill = 'limeGreen', border='black', borderWidth=1))
    
score = Label(0, 200, 40, size=50, fill='yellow', border='blue', borderWidth=2)

#Is the game over?
gameOver = False
onGround = True
canUpdateScore = True

def onStep():  #game loop
    global gameOver
    global onGround 
    global canUpdateScore
    if not gameOver:
        bird.centerY += 4
        bird.rotateAngle +=2
        if bird.rotateAngle > 100:
            bird.rotateAngle = 100

        if bird.bottom > 400:
            gameOver = True
            bird.fill = 'red'

        for i in range(4):            
            topPipes[i].centerX -= 4
            bottomPipes[i].centerX -= 4
            if bird.hitsShape(topPipes[i]) or bird.hitsShape(bottomPipes[i]):
                gameOver = True
                bird.fill = 'red'
            #check if block is off screen and recycle
            if topPipes[i].right < 0:
                topPipes[i].left = 1200
                topPipes[i].top = random.randint(-400,-100)
                bottomPipes[i].left = topPipes[i].left
                bottomPipes[i].top = topPipes[i].top + 400 + 100
                canUpdateScore = True
            if topPipes[i].left < bird.right and canUpdateScore:
                score.value += 1 #up the score
                canUpdateScore = False
        
    pass

def onKeyPress(key):
    global gameOver
    global onGround
    if (key == 'space'):
        bird.centerY -= 50
        bird.rotateAngle = 70


        



