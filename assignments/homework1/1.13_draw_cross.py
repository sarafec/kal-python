# todo: currently drawing with 4 lines can we draw it with two?

import turtle
turtle.pensize(5)
turtle.color("violet")

coordinatePairs = [[[0, -100], [0, 100]], [[0, 0], [0, 0]],[[-100, 0], [100, 0]], [[0,0], [0,0]]]

def drawLine(start, end):
	turtle.setposition(start[0], start[1])
	turtle.penup()
	turtle.goto(end[0], end[1])
	turtle.pendown()


for i in range(len(coordinatePairs)):
	drawLine(coordinatePairs[i][0], coordinatePairs[i][1])

turtle.done()