
class Enemy:
    '''def redrawAll(app, canvas):
        drawImageWithSizeBelowIt(app, canvas, app.image1, 200, 300)
        drawImageWithSizeBelowIt(app, canvas, app.image2, 500, 300)'''
    Size: int = 10

    def __init__(self, x, y, health, radius):
        self.health: int = health

        """
        positition of Enemy
        """
        self.x: int = x
        self.y: int = y
        self.radius = radius

    def isHit(self, player_missles) -> bool:
        '''
        iterates through the player missles and checks if the missiles are in the 
        enemy hitbox and returns a bool 
        '''
        self.health -= 1
        for missle_xy in player_missles:
            cx, cy = missle_xy [0], missle_xy [1]
            
            if (abs(cx - self.x) < self.hitBox and
                abs(cy - self.y) < self.hitBox):
                deleteEnemy()

            if (self.x, self.y) in missle_xy:
                return True
        return False

    # del enenmy fucnton
    # move funciton
    #
    # def move(self,)
