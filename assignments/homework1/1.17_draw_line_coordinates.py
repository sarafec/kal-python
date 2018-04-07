# todo: can the placement of the pen less redundant


import turtle
turtle.pensize(2)
turtle.color("black")

coordinates = [[-39, 48], [50, -50]]

def drawLine(coordinates):
	turtle.penup()
	turtle.goto(coordinates[0])
	turtle.pendown()
	turtle.goto(coordinates[1])
	turtle.penup()

	turtle.penup()
	turtle.goto(coordinates[0])
	turtle.pendown()
	turtle.write(str(coordinates[0][0]) + " , " + str(coordinates[0][1]))
	turtle.penup()
	turtle.goto(coordinates[1])
	turtle.pendown()
	turtle.write(str(coordinates[1][0]) + " , " + str(coordinates[1][1]))
	turtle.penup()

drawLine(coordinates)

turtle.done()