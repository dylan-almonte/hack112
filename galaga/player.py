from cmu_112_graphics import *

class Player(object):
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        # self.sprite = sprite
        # self.sizing = sizing
        self.lives = 3
        self.IsAlive = True
        self.IsHit = False
        self.bulletList = []

    def redraw(self, app, canvas):
        canvas.create_rectangle(self.cx-10, self.cy-10,self.cx+10,self.cy+10,
        fill = "blue", width = 3)

    def leftMove(self):
        if self.cx-10 > 250:
            self.cx -= 5

    def rightMove(self):
        if self.cx+10 < 750:
            self.cx += 5

    def fireBullet(self):
        bullet = [self.cx,self.cy-20,True]
        self.bulletList.append(bullet)

    def drawBullet(self, app, canvas):
        for bullet in self.bulletList:
            cx, cy, state = bullet
            if state:
                canvas.create_rectangle(cx-2.5, cy-5,
                                    cx+2.5,cy+5, fill = "yellow")

    def timerFired(self,app):
        for bullet in self.bulletList:
            bullet[1] -= 10
        

    

def appStarted(app):
    app.myPlayer = Player(500,450)

def keyPressed(app, event):
    if event.key == "Left":
        app.myPlayer.leftMove()
    elif event.key == "Right":
        app.myPlayer.rightMove()
    elif event.key == "Space":
        app.myPlayer.fireBullet()
    
def timerFired(app):
    app.timerDelay = 100
    app.myPlayer.timerFired(app)
    

def redrawAll(app, canvas):
    app.myPlayer.redraw(app,canvas)
    app.myPlayer.drawBullet(app, canvas)

runApp(width = 1000, height = 500)
