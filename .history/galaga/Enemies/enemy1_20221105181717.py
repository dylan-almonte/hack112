import cmu_112_graphics

def appStarted(app):
    app.enemyImage1 = app.loadImage('testImage2.gif')
    
def redrawAll(app, canvas):
    canvas.create_image(200, 300, image=ImageTk.PhotoImage(app.image1))