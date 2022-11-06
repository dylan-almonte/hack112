from cmu_112_graphics import *
from enemy import Enemy


class enemy1(Enemy):
    # TODO change to custom movements and timeToMove

    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0

        # self.moveBasic = [[1, 0]
        #                   [-1, 0]
        #                   [0, 1]]
        # self.timeToMove = 42

    def drawEnemy(self, canvas):
        canvas.create_oval(self.x-5, self.y-5, self.x+5, self.y+5,
                           fill='red')

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
