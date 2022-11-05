print("new")

from cmu_112_graphics import *

class Background(object):
    def __init__(self, width, height):
        self.width = width #width 500
        self.height = height #height 500

    def redraw(self, app, canvas):
        canvas.create_rectangle(app.width/4,0,app.width*3/4,app.height, fill = "black")

def appStarted(app):
    app.background = Background(500,500)

def redrawAll(app, canvas):
    app.background.redraw(app, canvas)
    



runApp(width = 1000,height = 500)
