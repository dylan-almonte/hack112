from cmu_112_graphics import *


def appStarted(app, size):
    app.hitBox = 5 #Change hitbox depending on enemy later //TODO
    app.enemyImage = app.loadImage('enemy_bumblebee.png')


def returnEnemyImage1(app):
    return ImageTk.PhotoImage(app.enemyImage)