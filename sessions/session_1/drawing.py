import turtle

# olympic symbol

turtle.pensize(5)

colors = ["blue", "black", "red", "yellow", "green"]
coordinatesPairs = [[-110, -25], [0, -25], [110, -25], [-55, -75], [55, -75]]

def drawCircle(color, coordinates):
	turtle.color(color)
	turtle.penup()
	turtle.goto(coordinates)
	turtle.pendown()
	turtle.circle(45)

for i in range(len(colors)):
	drawCircle(colors[i], coordinatesPairs[i])

turtle.done()


# questions
# 1 - is 'for i in range (len(colors))' idiomatic python?