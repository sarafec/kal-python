import turtle
turtle.pensize(5)
turtle.color("blue")

coordinates = [[40, -69.28], [-40, -69.28], [-80, -9.8], [-40, 69], [40, 60], [80, 0]]

def drawPolygon(coordinates):
	angle = 360 / len(coordinates)

	for side in range(len(coordinates)):
		turtle.forward(75)
		turtle.right(angle)

drawPolygon(coordinates)

turtle.done()