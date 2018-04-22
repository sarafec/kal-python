def getPentagonalNumber(num):
	pentagonalNum = int(num * ((3 * num) - 1) / 2)
	print(pentagonalNum)


for i in range(1, 100):
	getPentagonalNumber(i)