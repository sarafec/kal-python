import turtle

def drawBox(tile, x, y, size, fill):
	tile.penup()
	tile.goto(x,y)
	tile.pendown()

	tile.fillcolor(fill)
	tile.begin_fill()

	for i in range(0, 4):
		board.forward(size)
		board.right(90)

	tile.end_fill()


def drawChessboard(startX, startY, endX, endY):
	squareColor = "black"
	boxSize = int((endX-startX)/8)
	for i in range (0, 8):
		for j in range (0, 8):
			drawBox(board, startX + j * boxSize, startY + i * boxSize, boxSize, squareColor)
			squareColor = 'black' if squareColor == 'white' else 'white'

		squareColor = 'black' if squareColor == 'white' else 'white'

board = turtle.Turtle()
drawChessboard(0,0,80,80)
drawChessboard(90,0,180,180)
turtle.done()