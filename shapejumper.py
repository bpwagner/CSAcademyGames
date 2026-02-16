#shapeJumper
#Brian Wagner 2026
#www.codewithmrwagner.com
#This code works in the Sandbox area
#of CS Academy https://academy.cs.cmu.edu/


import random  #ability for random numbers
app.background = 'lavender'

#make shape and score board
dude = Rect(100,260,40,40, fill = 'gray')
score = Label(0, 200, 40, size=50, fill='green')
#make 5 blocks
blocks = []
for i in range(5):
    blocks.append( Rect(random.randint(400,2000), random.randint(200,280), \
        80, 30, fill = 'blue'))
        
spikes = []
for i in range(5):
    spikes.append( RegularPolygon(random.randint(400,2000), 290, 20, 3, fill = 'pink'))
        
ground = Rect(0,300,400,100)

#Is the game over?
gameOver = False
onGround = True
doubleJump = True
groundHeight = 280

def onStep():  #game loop
    global gameOver
    global onGround 
    global doubleJump
    global groundHeight
    
    if not gameOver:
        score.value += 1 #up the score
        
        dude.centerY += 3
        dude.rotateAngle += 5
        
        #dude is on the ground
        if dude.centerY > groundHeight:
            dude.centerY = groundHeight
            onGround = True
            doubleJump = True
        
        #check if we are on a block
        for block in blocks:
            if block.hitsShape(dude):
                onGround = True
                doubleJump = True
                groundHeight = block.top - 20
                break
            groundHeight = 280

        for block in blocks:            
            block.centerX -= 4
            #check if block is off screen and recycle
            if block.centerX < 0:
                block.centerX = random.randint(400,2000)
                block.top = random.randint(200,280)
                
        for spike in spikes:
            spike.centerX -= 6
            if spike.centerX < 0:
                spike.centerX = random.randint(400,2000)
                #check to see if we hit the block and if so, game over!
            if spike.hitsShape(dude):
                dude.fill = 'red'
                gameOver = True
        
    pass

def onKeyPress(key):
    global gameOver
    global onGround
    global doubleJump
    
    if (key == 'space'):
        if doubleJump:
            dude.centerY -= 80
            doubleJump = False
        elif onGround:
            dude.centerY -= 80
            onGround = False
            doubleJump = True
        



