from cmu_112_graphics import *
from enemy import Enemy

class enemy2:
    def __init__(self):
        #TODO change to custom movements
        self.moveBasic = [  [1, 0]
                            [-1, 0]
                            [0, 1]]
    def appStarted(app, size):
        app.hitBox = 5 #Change hitbox depending on enemy later //TODO
        app.enemyImage = app.loadImage('enemy_bumblebee.png')

def enemyImage(app):
        return ImageTk.PhotoImage(app.enemyImage)