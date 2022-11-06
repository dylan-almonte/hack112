print("new")

from cmu_112_graphics import *
import random

def newStar():
    colors = ['red', 'blue', 'yellow', 'orange', 'green', 'purple']
    cx = random.randint(250, 750)
    cy = 0
    colorIndex = random.randint(0, 5)
    starColor = colors[colorIndex]
    r = 1.5
    starState = 1
    return [cx, cy, r, starColor, starState]

class Background(object):
    def __init__(self, width, height):
        self.width = width #width 500
        self.height = height #height 500
        self.stars = []
        self.lives = 4

    def drawRect(self, app, canvas):
        canvas.create_rectangle(app.width/4,0, app.width*3/4, app.height, fill = "black")
    
    def drawStar(self, app, canvas, cx, cy, r, starColor, starState):
        if starState > 0:
            canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = f"{starColor}")
    
    def drawLife(self, app, canvas, tlx, tly, width):
        canvas.create_rectangle(tlx, tly, tlx+width, tly+width, fill = 'blue')
    
    def timerFired(self, app):
        for star in self.stars:
            star[1] += 5
            if star[1] > 500:
                self.stars.remove(star)
            star[4] *= -1
        star = newStar()
        self.stars.append(star)


def appStarted(app):
    app.background = Background(500,500)

def timerFired(app):
    app.timerDelay = 100
    app.background.timerFired(app)

def redrawAll(app, canvas):
    app.background.drawRect(app, canvas)
    print(len(app.background.stars))

    for star in app.background.stars:
        cx, cy, r, starColor, starState = star
        app.background.drawStar(app, canvas, cx, cy, r, starColor, starState)
    
    for x in range(app.background.lives):
        width = 30
        tlx = 260 + (40*x)
        tly = 460
        app.background.drawLife(app, canvas, tlx, tly, width)


runApp(width = 1000,height = 500)
