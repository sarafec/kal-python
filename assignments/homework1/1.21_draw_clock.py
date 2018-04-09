# todo: clear up redundancy and make a function that allows you to customize the hour/minute input

import turtle
turtle.pensize(5)
turtle.color("black")

startingCoordinates = [0,0]

def drawCircle(start):
	radiusSize = 100

	# clock outline
	turtle.penup()
	turtle.goto(start)
	turtle.pendown()
	turtle.circle(radiusSize)

	# clock annotations
	turtle.penup()
	turtle.goto(start[0], start[1] - 20 + (radiusSize * 2))
	turtle.pendown()
	turtle.write('12')
	turtle.penup()

	turtle.penup()
	turtle.goto(start[0], start[1] + 10)
	turtle.pendown()
	turtle.write('6')
	turtle.penup()

	turtle.penup()
	turtle.goto(start[0] - 10 + radiusSize, start[1] + radiusSize)
	turtle.pendown()
	turtle.write('3')
	turtle.penup()

	turtle.penup()
	turtle.goto(start[0] + 10 - radiusSize, start[1] + radiusSize)
	turtle.pendown()
	turtle.write('9')
	turtle.penup()


	# hour hand
	turtle.pensize(3)
	turtle.penup()
	turtle.goto(start[0], start[1] + radiusSize)
	turtle.pendown()
	turtle.goto(start[0] - radiusSize + 15, start[1] + radiusSize)

	# minute hand
	turtle.pensize(2)
	turtle.penup()
	turtle.goto(start[0], start[1] + radiusSize)
	turtle.pendown()
	turtle.goto(start[0] + radiusSize - 15, start[1] + radiusSize)


	# current time
	turtle.pensize(5)
	turtle.penup()
	turtle.goto(start[0], (start[1] - 25))
	turtle.pendown()
	turtle.write('9:15:00')
	turtle.penup()



drawCircle(startingCoordinates)

turtle.done()