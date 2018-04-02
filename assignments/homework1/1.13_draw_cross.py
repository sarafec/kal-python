import turtle
turtle.pensize(5)
turtle.color("violet")

coordinatePairs = [[[0, -100], [-200, -100]], [[-100, 0], [-100, -200]]]

def drawLine(start, end):
	turtle.setposition(start)
	turtle.penup()
	turtle.goto(end)
	turtle.pendown()


for i in range(len(coordinatePairs)):
	drawLine(coordinatePairs[i][0], coordinatePairs[i][1])

turtle.done()