from player import Player
from cmu_112_graphics import *
from Background import Background
# from enemyWave import EnemyWave
from enemyWave import EnemyWave
from enemy1 import enemy1
import time


def appStarted(app):
    # player ship
    # from: https://www.pngfind.com/mpng/iimowwo_galaga-galaga-ship-hd-png-download/
    app.playerImage = app.loadImage("playerShip.png")
    app.playerSprite = app.scaleImage(app.playerImage, 1/30)
    # lives
    app.playerLives = app.scaleImage(app.playerImage, 1/30)

    # explosion stages 1-4
    # all from: https://www.spriters-resource.com/fullview/26482/
    app.explode1 = app.loadImage("pExplosion_1.png")
    app.playerExplosion1 = app.scaleImage(app.explode1, 1/2.5)
    app.explode2 = app.loadImage("pExplosions_2.png")
    app.playerExplosion2 = app.scaleImage(app.explode2, 1/2.5)
    app.explode3 = app.loadImage("pExplosion_3.png")
    app.playerExplosion3 = app.scaleImage(app.explode3, 1/2.5)
    app.explode4 = app.loadImage("pExplosions_4.png")
    app.playerExplosion4 = app.scaleImage(app.explode4, 1/2.5)
    app.explosionAnimation = [
        app.playerExplosion1, app.playerExplosion2, app.playerExplosion3, app.playerExplosion4]

    # lives
    app.lives = app.loadImage('playerShip.png')
    app.finalLives = app.scaleImage(app.lives, 1/25)

    # bullet
    # from: https://toppng.com/photo/168502/alaga-galaga-missile
    app.bulletImage = app.loadImage("goodgalagamissile.png")
    app.playerBullet = app.scaleImage(app.bulletImage, 1/80)

    # temp
    # from: https://charactercommunity.fandom.com/wiki/Bumblebee
    app.enemyImage = app.loadImage("bumblebee.png")
    app.enemySprite = app.scaleImage(app.enemyImage, 1/10)

    app.background = Background(500, 500, app.finalLives)
    app.totalTime = 0
    app.myPlayer = Player(500, 450, app.playerSprite,
                          app.playerBullet, app.explosionAnimation)

    app.enemyWave = EnemyWave()

    app.bulletTime = 0
    app.bulletCounter = 0
    app.enemySpawnTime = 0

    # enemy explosions
    # from: https://www.spriters-resource.com/fullview/26482/
    app.enExplode1 = app.loadImage("enemyExplosion_1.png")
    app.enemyExplosion1 = app.scaleImage(app.enExplode1, 1/2)
    app.enExplode2 = app.loadImage("enemyExplosion_2.png")
    app.enemyExplosion2 = app.scaleImage(app.enExplode2, 1/2)
    app.enExplode3 = app.loadImage("enemyExplosion_3.png")
    app.enemyExplosion3 = app.scaleImage(app.enExplode3, 1/2)
    app.enExplode4 = app.loadImage("enemyExplosion_4.png")
    app.enemyExplosion4 = app.scaleImage(app.enExplode4, 1/2)
    app.enExplode5 = app.loadImage("enemyExplosion_5.png")
    app.enemyExplosion5 = app.scaleImage(app.enExplode5, 1/2)

    # enemy explosions
    # from: https://www.spriters-resource.com/fullview/26482/
    app.enExplode1 = app.loadImage("enemyExplosion_1.png")
    app.enemyExplosion1 = app.scaleImage(app.enExplode1, 1/2)
    app.enExplode2 = app.loadImage("enemyExplosion_2.png")
    app.enemyExplosion2 = app.scaleImage(app.enExplode2, 1/2)
    app.enExplode3 = app.loadImage("enemyExplosion_3.png")
    app.enemyExplosion3 = app.scaleImage(app.enExplode3, 1/2)
    app.enExplode4 = app.loadImage("enemyExplosion_4.png")
    app.enemyExplosion4 = app.scaleImage(app.enExplode4, 1/2)
    app.enExplode5 = app.loadImage("enemyExplosion_5.png")
    app.enemyExplosion5 = app.scaleImage(app.enExplode5, 1/2)

    app.score = 0

    # start screen
    app.menu = app.loadImage("startScreen.png")
    # from: https://downloads.khinsider.com/game-soundtracks/album/galaga-arcade
    app.menuPicture = app.scaleImage(app.menu, 1/2)
    app.startMenu = True
    app.gameOver = False

    app.enemyTime = 0
    app.tempPlayerCoors = []


def timerFired(app):
    app.enemySpawnTime += 1
    if app.enemySpawnTime - 10 == 0:
        app.enemyWave.spawnEnemy(app)
        app.enemySpawnTime = 0
    # print((app.enemy.time - app.enemy.curveTime)%app.enemy.period)
    app.enemyWave.moveEnemies()
    if app.gameOver == False:
        if app.background.lives == 0:
            app.gameOver = True
        # app.enemyWave.spawnEnemy(app)

        # print((app.enemy.time - app.enemy.curveTime)%app.enemy.period)
        app.background.timerFired(app)
        app.background.newStar(app)
        app.bulletTime += 1
        if app.bulletTime % 5 == 0:
            app.bulletCounter = 0
        app.myPlayer.timerFired(app)
        # app.enemy.bulletMovement(app, app.myPlayer.cx, app.myPlayer.cy)
        for bullet in EnemyWave.bulletList:
            app.myPlayer.playerIsHit(bullet, app.background)

        app.enemyTime += 1
        app.enemyTime %= 1000
        if app.enemyWave.updateScore(app.myPlayer.bulletList):
            app.score += 20
        app.enemyWave.EnemyHit(app.myPlayer.bulletList)
        

def keyPressed(app, event):
    # temp
    if app.gameOver == False:
        if event.key == "Left":
            app.myPlayer.leftMove()
        elif event.key == "Right":
            app.myPlayer.rightMove()
        elif event.key == "Space":
            if app.bulletCounter < 2:
                app.bulletCounter += 1
                app.myPlayer.fireBullet()
        elif event.key == 'p':
            app.startMenu = False
        elif event.key == 'r':
            app.startMenu = True
            app.gameOver = False


def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill="grey6")
    app.background.drawRect(app, canvas)

    for star in app.background.stars:
        cx, cy, r, starColor, starState = star
        app.background.drawStar(app, canvas, cx, cy, r, starColor, starState)

    if app.startMenu == False and app.gameOver == False:

        for x in range(app.background.lives):
            cx = 280 + (40*x)
            cy = 480
            app.background.drawLife(app, canvas, cx, cy)

        app.myPlayer.redraw(app, canvas)
        app.myPlayer.redrawExplosion(app, canvas)
        app.myPlayer.drawBullet(app, canvas)

        app.enemyWave.drawEnemies(app, canvas)
        # app.enemy.drawBullet(app,canvas)

    if app.startMenu == True:
        canvas.create_image(
            500, 150, image=ImageTk.PhotoImage(app.menuPicture))

        canvas.create_text(500, 250, text="P r e s s  'P'  T o  P l a y",
                           font="system 15 bold italic", fill='red')

    if app.gameOver == True:
        canvas.create_text(500, 250, text="G A M E  O V E R",
                           font="system 25 bold", fill='red')
        canvas.create_text(500, 350, text="Press 'r' to restart", fill='red')

    canvas.create_text(100, 50, text=f"SCORE:\n      {app.score}",
                       font="system 20 bold", fill="grey30")


runApp(width=1000, height=500)
