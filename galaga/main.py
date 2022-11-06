from player import Player
from cmu_112_graphics import *
from Background import Background


def appStarted(app):
    app.background = Background(500, 500)
    app.totalTime = 0
    app.myPlayer = Player(500, 450)


def timerFired(app):
    app.background.timerFired(app)
    app.background.newStar(app)
    app.myPlayer.timerFired(app)


def keyPressed(app, event):
    if event.key == "Left":
        app.myPlayer.leftMove()
    elif event.key == "Right":
        app.myPlayer.rightMove()
    elif event.key == "Space":
        app.myPlayer.fireBullet()


def redrawAll(app, canvas):

    app.background.drawRect(app, canvas)

    for star in app.background.stars:
        cx, cy, r, starColor, starState = star
        app.background.drawStar(app, canvas, cx, cy, r, starColor, starState)

    for x in range(app.background.lives):
        width = 30
        tlx = 260 + (40*x)
        tly = 460
        app.background.drawLife(app, canvas, tlx, tly, width)

    app.myPlayer.redraw(app, canvas)
    app.myPlayer.drawBullet(app, canvas)


runApp(width=1000, height=500)
