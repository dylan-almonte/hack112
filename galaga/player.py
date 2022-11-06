from cmu_112_graphics import *


class Player(object):
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.radius = 10
        # self.sprite = sprite
        # self.sizing = sizing
        self.lives = 3
        self.IsAlive = True
        self.IsHit = False
        self.bulletList = []

    def redraw(self, app, canvas):
        canvas.create_rectangle(self.cx-self.radius, self.cy-self.radius,
                                self.cx+self.radius, self.cy+self.radius,
                                fill="blue", width=3)

    def leftMove(self):
        if self.cx-10 > 250:
            self.cx -= 10

    def rightMove(self):
        if self.cx+10 < 750:
            self.cx += 10

    def fireBullet(self):
        bullet = [self.cx, self.cy-20, True]
        self.bulletList.append(bullet)

    def drawBullet(self, app, canvas):
        for bullet in self.bulletList:
            cx, cy, state = bullet
            if state:
                canvas.create_rectangle(cx-2.5, cy-5,
                                        cx+2.5, cy+5, fill="yellow")

    def timerFired(self, app):
        for bullet in self.bulletList:
            if bullet[1] + 5 < 0:
                self.bulletList.remove(bullet)
            bullet[1] -= 15

    def playerIsHit(self, enemyMissiles):
        for missile in enemyMissiles:
            cx, cy = missile[0], missile[1]

            if (abs(cx - self.cx) < self.radius and
                    abs(cy - self.cy) < self.radius):
                return True
        return False


def appStarted(app):
    app.myPlayer = Player(500, 450)
    app.bulletCounter = 0
    app.time = 0


def keyPressed(app, event):
    if event.key == "Left":
        app.myPlayer.leftMove()
    elif event.key == "Right":
        app.myPlayer.rightMove()
    elif event.key == "Space":
        if app.bulletCounter < 2:
            app.bulletCounter += 1
            app.myPlayer.fireBullet()


def timerFired(app):
    app.time += 1
    if app.time % 5 == 0:
        app.bulletCounter = 0
    app.myPlayer.timerFired(app)


def redrawAll(app, canvas):
    app.myPlayer.redraw(app, canvas)
    app.myPlayer.drawBullet(app, canvas)

# runApp(width = 1000, height = 500)
