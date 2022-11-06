from player import Player
from cmu_112_graphics import *
from Background import Background
# from enemyWave import EnemyWave
from enemy import Enemy


def appStarted(app):
    app.playerImage = app.loadImage("playerShip.png")
    app.playerSprite = app.scaleImage(app.playerImage, 1/30)

    app.playerLives = app.scaleImage(app.playerImage, 1/30)

    # bullet 
    app.bulletImage = app.loadImage("goodgalagamissile")
    app.playerBullet = app.scaleImage(app.bulletImage, 1/20)

    # temp
    app.enemyImage = app.loadImage("bumblebee.png")
    app.enemySprite = app.scaleImage(app.enemyImage, 1/2)

    app.background = Background(500, 500)
    app.totalTime = 0
    app.myPlayer = Player(500, 450, app.playerSprite)

    app.enemy = Enemy(500, 20, app.enemySprite)

    app.bulletTime = 0
    app.bulletCounter = 0


def timerFired(app):
    # app.enemyWave.spawnEnemy(app)
    app.background.timerFired(app)
    app.background.newStar(app)
    app.bulletTime += 1
    if app.bulletTime % 5 == 0:
        app.bulletCounter = 0
    app.myPlayer.timerFired(app)
    app.enemy.bulletMovement(app, app.myPlayer.cx, app.myPlayer.cy)


def keyPressed(app, event):
    # temp
    if event.key == 'e':
        app.enemy.fireBullet()

    if event.key == "Left":
        app.myPlayer.leftMove()
    elif event.key == "Right":
        app.myPlayer.rightMove()
    elif event.key == "Space":
        if app.bulletCounter < 2:
            app.bulletCounter += 1
            app.myPlayer.fireBullet()

def redrawAll(app, canvas):
    canvas.create_rectangle(0,0,app.width,app.height, fill = "grey6")
    app.background.drawRect(app, canvas)

    for star in app.background.stars:
        cx, cy, r, starColor, starState = star
        app.background.drawStar(app, canvas, cx, cy, r, starColor, starState)

    for x in range(app.background.lives):
        cx = 280 + (40*x)
        cy = 480
        app.background.drawLife(app, canvas, cx, cy, app.playerLives)

    app.myPlayer.redraw(app, canvas)
    app.myPlayer.drawBullet(app, canvas)

    app.enemy.redraw(app, canvas)
    app.enemy.drawBullet(app, canvas)


runApp(width=1000, height=500)
