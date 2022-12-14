from cmu_112_graphics import *
import random


class Background(object):
    def __init__(self, width, height, sprite):
        self.width = width  # width 500
        self.height = height  # height 500
        self.stars = []
        self.lives = 4 
        self.sprite = sprite

    def drawRect(self, app, canvas):
        canvas.create_rectangle(
            app.width/4, 0, app.width*3/4, app.height, fill="black")

    def newStar(self, app):
        colors = ['red', 'blue', 'yellow', 'orange', 'green', 'purple']
        cx = random.randint(250, 750)
        cy = 0
        colorIndex = random.randint(0, 5)
        starColor = colors[colorIndex]
        r = 1.5
        starState = 1
        self.stars.append([cx, cy, r, starColor, starState])

    def drawStar(self, app, canvas, cx, cy, r, starColor, starState):
        for star in self.stars:
            cx, cy, r, starColor, starState = star
            if starState > 0:
                canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=f"{starColor}")
        

    def drawLife(self, app, canvas, cx, cy):
        canvas.create_image(cx, cy, image = ImageTk.PhotoImage(self.sprite))

    def timerFired(self, app):
        app.totalTime += 1
        for star in self.stars:
            star[1] += 30
            if star[1] > 500:
                self.stars.remove(star)
            star[4] *= -1


def appStarted(app):
    app.background = Background(500, 500)
    app.totalTime = 0



def timerFired(app):
    app.background.timerFired(app)
    app.background.newStar(app)


def redrawAll(app, canvas):
    app.background.drawRect(app, canvas)

    for star in app.background.stars:
        cx, cy, r, starColor, starState = star
        app.background.drawStar(app, canvas, cx, cy, r, starColor, starState)

    for x in range(app.background.lives):
        cx = 280 + (50*x)
        cy = 470
        app.background.drawLife(app, canvas, cx, cy, app.finalLives)

# runApp(width = 1000,height = 500)
