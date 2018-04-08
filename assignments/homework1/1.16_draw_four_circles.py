import turtle
turtle.pensize(5)
turtle.color("purple")

startingCoordinates = [[-50,0], [50,0], [-50, -100], [50, -100]]

def drawCircle(start):
	turtle.penup()
	turtle.goto(start)
	turtle.pendown()
	turtle.circle(50)



for i in range(len(startingCoordinates)):
	drawCircle(startingCoordinates[i])

turtle.done()