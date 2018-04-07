import turtle
turtle.pensize(5)
turtle.color("blue")

def drawStar():
	angle = 140

	for side in range(5):
		turtle.forward(75)
		turtle.right(angle)
		turtle.forward(75)
		turtle.right(72 - angle)

drawStar()

turtle.done()