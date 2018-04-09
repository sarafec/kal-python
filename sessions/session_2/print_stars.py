numOfRows = int(input("How many stars would you like to print?\n"))
numOfCol = numOfRows

def printStarRow():
	for star in range (numOfCol):
		print("*", end = ' ')
	print()


for star in range (numOfRows):
	printStarRow()
	numOfCol -= 1