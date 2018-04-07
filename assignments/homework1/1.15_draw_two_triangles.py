import turtle
turtle.pensize(5)
turtle.color("red")

triangleCoordinates = [[[0,0], [60, -100], [-60, -100], [0,0]], [[0,0], [-60, 100], [60, 100], [0,0]]]

def drawTriangle(coordinates):
	turtle.penup()
	turtle.goto(coordinates[0])
	turtle.pendown()
	turtle.goto(coordinates[1])
	turtle.pendown()
	turtle.goto(coordinates[2])
	turtle.pendown()
	turtle.goto(coordinates[3])
	turtle.pendown()



for i in range(len(triangleCoordinates)):
	drawTriangle(triangleCoordinates[i])

turtle.done()