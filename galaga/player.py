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

    
    def redraw(self, app, canvas):
        canvas.create_rectangle(self.cx-10, self.cy-10,self.cx+10,self.cy+10,
        fill = "blue", widht = 3)

    



def redrawAll(app, canvas):
    pass



runApp(width = 1000, height = 500)

