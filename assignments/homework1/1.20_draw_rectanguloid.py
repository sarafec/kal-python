import turtle
turtle.pensize(5)
turtle.color("green")

# todo: draw coordinates
polygonCoordinates = []
connectingLines = []

def drawRectanguloid(coordinates):
	angle = 360 / len(coordinates)

	for side in range(len(coordinates)):
		turtle.forward(75)
		turtle.right(angle)

drawRectanguloid(coordinates)

turtle.done()