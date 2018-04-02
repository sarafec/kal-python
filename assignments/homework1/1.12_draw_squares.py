import turtle
turtle.pensize(5)
turtle.color("purple")

coordinatePairs = [[0, 0], [-50, 0], [-50, -50], [0, -50]]

def drawCircle(coordinates):
	turtle.setposition(coordinates)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)
	turtle.forward(50)
	turtle.left(90)


for i in range(len(coordinatePairs)):
	drawCircle(coordinatePairs[i])

turtle.done()
