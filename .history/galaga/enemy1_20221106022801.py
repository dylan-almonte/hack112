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

    def __init__(self, x, y, sprite):
        super().__init__(x, y, sprite)
        self.x = 0
        self.y = 0
        

        # self.moveBasic = [[1, 0]
        #                   [-1, 0]
        #                   [0, 1]]
        # self.timeToMove = 42

    def drawEnemy(self, canvas):
        canvas.create_oval(self.x-5, self.y-5, self.x+5, self.y+5,
                           fill='red')

    def updateEnemyXpos(self):
        time = self.time
        tInit = enemy1.curveTime
        moveRightTime = enemy1.horizontalTime
        moveDownTime = moveRightTime + enemy1.verticalTime
        moveLeftTime = moveDownTime + enemy1.horizontalTime
        period = moveLeftTime
        
        # if time <= tInit and enemy1.curve == True:
        #     x = enemy1.boardRight - enemy1.curveRad * math.sin(time/20)
        # else:
        #     enemy1.curve = False

        # time = time - tInit

        # if time % period <= moveRightTime:
        #     x = enemy1.leftCol + enemy1.dx * time
        # elif time % period <= moveDownTime:
        #     x = enemy1.rightCol
        # elif time % period <= moveLeftTime:
        #     x = enemy1.rightCol - enemy1.dx * time
        # elif time % period <= period:
        #     x = enemy1.leftCol

        x = (enemy1.rightCol + enemy1.leftCol)/2 + 225 * math.sin(time/20)
        self.x = x
            
def updateEnemyYpos(self):
        oldY = 0
        tInit = enemy1.curveTime
        time = self.time
        moveOverTime = enemy1.horizontalTime
        moveDownTime = moveOverTime + enemy1.verticalTime
        period = moveDownTime
        

        # if time <= tInit:
        #     yPos = enemy1.topRow - enemy1.curveRad * math.cos(time/20)
        
        # time = time - tInit
       
        if time % period == moveDownTime:
            self.y += 13
        

    # def appStarted(app):
    #     app.hitBox = 5 #Change hitbox depending on enemy later //TODO
    #     app.enemyImage = app.loadImage('enemy_bumblebee.png')

    # def enemyImage(app):
    #     return ImageTk.PhotoImage(app.enemyImage)

    # def getVel(self, time):
    #     if time % self.timeToMove == 1:
    #         return self.moveBasic[0]

    #     if time % self.timeToMove == 2:
    #         return self.moveBasic[1]

    #     if time % self.timeToMove == 3:
    #         return self.moveBasic[2]
