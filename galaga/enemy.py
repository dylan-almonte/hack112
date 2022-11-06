from player import Player
from cmu_112_graphics import *


class Enemy:
    '''def redrawAll(app, canvas):
        drawImageWithSizeBelowIt(app, canvas, app.image1, 200, 300)
        drawImageWithSizeBelowIt(app, canvas, app.image2, 500, 300)'''

    def __init__(self, x, y, app):
        self.health: int = 2
        self.time = 0
        """
        positition of Enemy
        """
        self.x: int = x
        self.y: int = y
        self.size: int = 30
        self.bullets: list = []
        self.xi = self.x
        self.yi = self.y

        # temporaty

    def isHit(self, player_missles) -> bool:
        '''
        iterates through the player missles and checks if the missiles are in the 
        enemy hitbox and returns a bool 
        '''
        for missle_xy in player_missles:
            cx, cy = missle_xy[0], missle_xy[1]
            if (abs(cx - self.x) < self.size and
                    abs(cy - self.y) < self.size):
                self.health -= 1
                return True
                #health - 1

        return False
# In the game class, if health == 0, delete Enemy

    # def move(self, velocity):
    #     xVel, yVel = velocity[0], velocity[1]
    #     self.x += xVel
    #     self.y += yVel
    # TODO  create a different function that updates the enmeny posistion

    def redraw(self, app, canvas):
        canvas.create_image(
            self.x, self.y, image=ImageTk.PhotoImage(self.sprite))

    def updateEnemyTime(self):
        self.time += 2

    def fireBullet(self, px, py):
        bullet = [self.x, self.y, self.x-px, py]
        self.bullets.append(bullet)

    def drawBullet(self, app, canvas):
        for b in self.bullets:
            x, y = b[0], b[1]
            r = 5
            canvas.create_oval(x-r, y-r, x+r, y+r, fill='red')

    def bulletMovement(self, app):  # timer fired

        for b in self.bullets:
            # dx, dy = dx/100, dy
            b[0] -= b[2]/20
            b[1] += b[3]/20
            if b[1] > app.height or b[1] < 0 or b[0] > 750 or b[0] < 250:
                self.bullets.remove(b)

    # del enenmy fucnton
    # move funciton
    #
    # def move(self,)

    # def deleteEnemy()
    # pop enemy
