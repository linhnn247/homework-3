from turtle import *
#speed(-1)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
def drawpolygon(sz,sd):
    for i in range(sd):
        forward(sz)
        left(360/sd)

for i in range (7,2,-1):
    clr = colors[7-i]
    pencolor(clr)
    fillcolor(clr)
    begin_fill()
    drawpolygon(100,i)
    end_fill()
hideturtle()
mainloop()