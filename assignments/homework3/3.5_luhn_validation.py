# luhn validation


def isValid(num):
	numList = list(map(int,str(num)))
	morphDigits(numList)
	totalSum = sumOfEvenPlace(numList) + sumofOddPlace(numList)
	print(totalSum % 10 == 0)

# todo: clean up this fn
def morphDigits(numList):
	for i in range(0, len(numList)):
		if i % 2 == 0:
			numList[i] = numList[i] * 2
			while numList[i] > 9:
				tempList = list(map(int,str(numList[i])))
				sum = 0
				for num in tempList:
					sum = sum + num 
				numList[i] = sum

def sumOfEvenPlace(numList):
	tempList = []
	for i in range(0, len(numList)):
		if i % 2 == 0:
			tempList.append(numList[i])
	return sumElements(tempList)


def sumofOddPlace(numList):
	tempList = []
	for i in range(0, len(numList)):
		if i % 2 == 1:
			tempList.append(numList[i])
	return sumElements(tempList)


def sumElements(list):
	sum = 0
	for elem in list:
		sum = sum + elem
	return sum


isValid(4388576018402626)