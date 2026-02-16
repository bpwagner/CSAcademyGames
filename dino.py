#dino
#Brian Wagner 2026
#www.codewithmrwagner.com
#This code works in the Sandbox area
#of CS Academy https://academy.cs.cmu.edu/


import random  #ability for random numbers
app.background = 'white'

#make dino and score board
dino = Oval(100,280,20,40, fill = 'green')
score = Label(0, 200, 40, size=18, fill='blue')
#make 5 blocks
blocks = []
for i in range(5):#bounce3
#Brian Wagner 2026
#www.codewithmrwagner.com
    blocks.append( Rect(random.randint(400,2000), 280, \
        40, 30, fill = 'blue'))
        
ground = Rect(0,300,400,100)
ceiling = Rect(0,0,400,150, fill='yellow')

#Is the game over?
gameOver = False

def onStep():  #game loop
    global gameOver
    
    if not gameOver:
        score.value += 1 #up the score
        
        dino.centerY += 3
        if dino.centerY > 280:
            dino.centerY = 280
        
        for block in blocks:
            
            block.centerX -= 4
            #check if block is off screen and recycle
            if block.centerX < 0:
                block.centerX = random.randint(400,500)
                
            #check to see if we hit the block and if so, game over!
            if block.hitsShape(dino):
                dino.fill = 'red'
                gameOver = True

    pass

def onKeyPress(key):
    global gameOver
    if (key == 'space'):
        dino.centerY -= 30
        
    if dino.centerY < 150:
        dino.fill = 'red'
        gameOver = True


