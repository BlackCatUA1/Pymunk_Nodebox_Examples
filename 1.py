from nodebox.graphics import *

def draw(canvas):
    background(1)
    translate(250, 250)
    rotate(canvas.frame)
    rect(-100, -100, 100, 100)

canvas.size = 500, 500
canvas.run(draw)
