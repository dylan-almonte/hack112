from cmu_112_graphics import *
import time
from Background import Background

class Player(object):
    def __init__(self, cx, cy, sprite, bulletSprite, explosionSprite):
        self.cx = cx
        self.cy = cy
        self.radius = 23
        self.sprite = sprite
        self.IsHit = False
        self.IsInvulnerable = False
        self.bulletList = []
        self.bulletSprite = bulletSprite
        self.baseTime = 0
        self.explosionSprite = explosionSprite
        self.blank = False
        self.exploSprite = self.explosionSprite[0]


        

    def redraw(self, app, canvas):
        if self.IsHit == False:
            canvas.create_image(self.cx,self.cy, 
            image = ImageTk.PhotoImage(self.sprite))

    def redrawExplosion(self, app, canvas):
        if self.blank == True:
            pass
        elif self.IsHit == True:
            canvas.create_image(self.cx,self.cy,image = ImageTk.PhotoImage(self.exploSprite))
        



    def leftMove(self):
        if self.IsHit == False:
            if self.cx-self.radius > 250:
                self.cx -= 10

    def rightMove(self):
        if self.IsHit == False:
            if self.cx+self.radius < 750:
                self.cx += 10


    def fireBullet(self):
        if self.IsHit == False:
            bullet = [self.cx, self.cy-20, True]
            self.bulletList.append(bullet)

    def drawBullet(self, app, canvas):
        for bullet in self.bulletList:
            cx, cy, state = bullet
            if state:
                canvas.create_image(cx,cy, image = ImageTk.PhotoImage(self.bulletSprite))

    def timerFired(self, app):
        if self.IsHit == True:
            self.hitTimer = time.time()
            elapsedTime = (self.hitTimer-self.baseTime)
            if elapsedTime < .1:
                self.exploSprite = self.explosionSprite[0]
            elif elapsedTime < .2:
                self.exploSprite = self.explosionSprite[1]
            elif elapsedTime < .3:
                self.exploSprite = self.explosionSprite[2]
            elif elapsedTime < .4:
                self.exploSprite = self.explosionSprite[3]
            elif elapsedTime < .6:
                self.blank = True
            else:
                self.IsHit, self.blank = False, False


        for bullet in self.bulletList:
            if bullet[1] + 5 < 0:
                self.bulletList.remove(bullet)
            bullet[1] -= 30

    def playerIsHit(self, enemyMissiles, background):
        if self.IsHit == False:
            for missile in enemyMissiles:
                cx, cy = missile[0], missile[1]
                if (abs(cx - self.cx) < self.radius and abs(cy - self.cy) < self.radius):
                    self.IsHit = True
                    background.lives -= 1
                    self.baseTime = time.time()
                    return True
            return False
    
    def playerInvulnerability(self, timer):
        pass


# def appStarted(app):
#     app.image = app.loadImage("playerShip.png")
#     app.sprite = app.scaleImage(app.image, 1/10)
#     app.myPlayer = Player(500, 450, app.sprite)
#     app.bulletCounter = 0
#     app.time = 0


# def keyPressed(app, event):
#     if event.key == "Left":
#         app.myPlayer.leftMove()
#     elif event.key == "Right":
#         app.myPlayer.rightMove()
#     elif event.key == "Space":
#         if app.bulletCounter < 2:
#             app.bulletCounter += 1
#             app.myPlayer.fireBullet()


# def timerFired(app):
#     app.time += 1
#     if app.time % 2 == 0:
#         app.bulletCounter = 0
#     app.myPlayer.timerFired(app)


# def redrawAll(app, canvas):
#     app.myPlayer.redraw(app, canvas)
#     app.myPlayer.drawBullet(app, canvas)

# runApp(width = 1000, height = 500)
