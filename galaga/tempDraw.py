print("new")

from cmu_112_graphics import *
import random

class Background(object):
    def __init__(self, width, height):
        self.width = width #width 500
        self.height = height #height 500
        self.stars = []

    def drawRect(self, app, canvas):
        canvas.create_rectangle(app.width/4,0,app.width*3/4,app.height, fill = "black")

    def newStar(self, app, canvas):
        colors = ['red', 'blue', 'yellow', 'orange', 'green']
        cx = random.randint(250, 750)
        cy = 0 
        colorIndex = random.randint(0, 4)
        starColor = colors[colorIndex]
        r = 2
        self.stars.append([cx, cy, r, starColor])
    
    def drawStar(self, app, canvas, cx, cy, r, starColor):
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = f"{starColor}")

    
    def timerFired(app):
        pass
        

def appStarted(app):
    app.background = Background(500,500)



    


def redrawAll(app, canvas):
    app.background.drawRect(app, canvas)
    for star in app.background.stars():
        pass



    



runApp(width = 1000,height = 500)
