from cmu_112_graphics import *


def appStarted(app):
    app.enemyImage1 = app.loadImage('enemy_bumblebee.png')
    
def redrawAll(app, canvas):
    canvas.create_image(200, 300, image=ImageTk.PhotoImage(app.image1))