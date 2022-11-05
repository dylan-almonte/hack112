from cmu_112_graphics import *

class Background(object):
    def __init__(self, width, height):
<<<<<<< HEAD
        self.width = width
        self.height = height # this is the height
        
    
=======
        self.width = width #width 500
        self.height = height #height 500

    def redraw(self, app, canvas):
        canvas.create_rectangle(app.width/4,0,app.width*3/4,app.height, fill = "black")



>>>>>>> 1698aa90efc7c7789157bf05b7aada085e52df24
