from turtle import *
#speed(-1)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
def drawbar(h,w):
    right(90)
    forward(h)
    left(90)
    forward(w)
    left(90)
    forward(h)
    right(90)

for i in range(5):
    clr = colors[i]
    pencolor(clr)
    fillcolor(clr)
    begin_fill()
    drawbar(100,50)
    end_fill()

mainloop()