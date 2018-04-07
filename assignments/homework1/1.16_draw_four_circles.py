import turtle
turtle.pensize(5)
turtle.color("purple")

startingCoordinates = [[-50,0], [50,0], [-50, -100], [50, -100]]

def drawTriangle(start):
	turtle.penup()
	turtle.goto(start)
	turtle.pendown()
	turtle.circle(50)



for i in range(len(startingCoordinates)):
	drawTriangle(startingCoordinates[i])

turtle.done()