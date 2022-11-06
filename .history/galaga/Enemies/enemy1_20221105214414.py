from cmu_112_graphics import *
from enemy import Enemy

class enemy1:
    #TODO change to custom movements and timeToMove
    
    
    def __init__(self, x, y):
        super().__init__(x, y, 1, 20)
        self.x = x
        self.y = y

        self.moveBasic = [[1, 0]
                        [-1, 0]
                        [0, 1]]
        self.timeToMove = 42


    def appStarted(app):
        app.hitBox = 5 #Change hitbox depending on enemy later //TODO
        app.enemyImage = app.loadImage('enemy_bumblebee.png')

    def enemyImage(app):
        return ImageTk.PhotoImage(app.enemyImage)
    
    def getVel(self, time):
        if time % self.timeToMove == 1:
            return self.moveBasic [0]

        if time % self.timeToMove == 2:
            return self.moveBasic [1]

        if time % self.timeToMove == 3:
            return self.moveBasic [2]


    