from cmu_112_graphics import *

class Background(object):
    def __init__(self, width, height):
        self.width = width #width 500
        self.height = height #height 500

    def redraw(self, app, canvas):
        canvas.create_rectangle(app.width/4,0,app.width*3/4,app.height, fill = "black")




GalagaBackground = Background(500,500)

def runGalaga(app, canvas):
    runApp()
    GalagaBackground.redraw(app, canvas)
