from cmu_112_graphics import *
from enemy import Enemy
import math

class enemy1(Enemy):
    # TODO change to custom movements and timeToMove
    curveTime = 20

    horizontalTime = 20
    verticalTime = 2
    period = 2 * horizontalTime + 2 * verticalTime

    boardRight = 750
    boardLeft = 250
    boardTop = 0
    boardBot = 500

    rightCol = boardRight - 25
    leftCol = boardLeft + 25
    topRow = boardTop + 25
    botRow = boardBot - 25
    
    curveRad = rightCol - leftCol

    curve = False
    dx = (boardRight - boardLeft)/horizontalTime
    dy = 30/2

    def __init__(self, x, y, app):
        super().__init__(x, y, app)
        self.x = 0
        self.y = 0
        #Enemy image
        self.sprite = app.loadImage('bumblebee.png')
        app.enemyImage = app.scaleImage(self.sprite, 1/4)
        

        # self.moveBasic = [[1, 0]
        #                   [-1, 0]
        #                   [0, 1]]
        # self.timeToMove = 42



    def drawEnemy(self, app, canvas):
        canvas.create_image(self.x, self.y,
        image = ImageTk.PhotoImage(app.enemyImage))

    def updateEnemyXpos(self):
        time = self.time 
        x = (enemy1.rightCol + enemy1.leftCol)/2 + 225 * math.sin(time/20)
        self.x = x
            
    def updateEnemyYpos(self):
        time = self.time
        period = 40
        
        if time % period == 0:
            self.y += 13
        