from player import Player
from cmu_112_graphics import *
from Background import Background
# from enemyWave import EnemyWave
from enemy import Enemy
from enemy1 import enemy1
from Score import Score

def appStarted(app):
    # player ship
    app.playerImage = app.loadImage("playerShip.png")
    app.playerSprite = app.scaleImage(app.playerImage, 1/30)
        # lives
    app.playerLives = app.scaleImage(app.playerImage, 1/30)

        # explosion stages 1-4
    app.explode1 = app.loadImage("pExplosion_1.png")
    app.playerExplosion1 = app.scaleImage(app.explode1, 1/10)
    app.explode2 = app.loadImage("pExplosions_2.png")
    app.playerExplosion2 = app.scaleImage(app.explode2, 1/10)
    app.explode3 = app.loadImage("pExplosion_3.png")
    app.playerExplosion3 = app.scaleImage(app.explode3, 1/10)
    app.explode4 = app.loadImage("pExplosions_4.png")
    app.playerExplosion4 = app.scaleImage(app.explode4, 1/10)


    # bullet 
    app.bulletImage = app.loadImage("goodgalagamissile.png")
    app.playerBullet = app.scaleImage(app.bulletImage, 1/80)

    # temp
    app.enemyImage = app.loadImage("bumblebee.png")
    app.enemySprite = app.scaleImage(app.enemyImage, 1/10)

    app.background = Background(500, 500)
    app.totalTime = 0
    app.myPlayer = Player(500, 450, app.playerSprite, app.playerBullet)

    app.enemy = enemy1(0, 0, app.enemySprite)

    app.bulletTime = 0
    app.bulletCounter = 0

    app.hitTimer = 0

    app.score = Score()




def timerFired(app):
    # app.enemyWave.spawnEnemy(app)
    app.enemy.updateEnemyTime()
    app.enemy.updateEnemyXpos()
    app.enemy.updateEnemyYpos()
    print((app.enemy.time - app.enemy.curveTime)%app.enemy.period)
    app.background.timerFired(app)
    app.background.newStar(app)
    app.bulletTime += 1
    if app.bulletTime % 5 == 0:
        app.bulletCounter = 0
    app.myPlayer.timerFired(app)
    app.enemy.bulletMovement(app, app.myPlayer.cx, app.myPlayer.cy)
    if app.myPlayer.playerIsHit(app.enemy.bullets) == True:
        pass




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

    canvas.create_text(100, 50, text= f"SCORE:\n      {app.score.score}",
                        font = "system 20 bold", fill = "grey30")

runApp(width=1000, height=500)
