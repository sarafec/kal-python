# luhn validation

def isValid(num):
	numList = list(map(int,str(num)))
	morphDigits(numList)
	totalSum = sumOfEvenPlace(numList) + sumofOddPlace(numList)
	print(isDivisibleByTen(totalSum))

def morphDigits(numList):
	for i in range(0, len(numList)):
		if isEven(i):
			numList[i] = numList[i] * 2
			while numList[i] > 9:
				tempList = list(map(int,str(numList[i])))
				numList[i] = sumElements(tempList)

def sumOfEvenPlace(numList):
	tempList = []
	for i in range(0, len(numList)):
		if isEven(i):
			tempList.append(numList[i])
	return sumElements(tempList)


def sumofOddPlace(numList):
	tempList = []
	for i in range(0, len(numList)):
		if isOdd(i):
			tempList.append(numList[i])
	return sumElements(tempList)



### Utility Functions ###
def isOdd(num):
	if num % 2 == 1:
		return True
	else:
		return False

def isEven(num):
	if num % 2 == 0:
		return True
	else: 
		return False

def isDivisibleByTen(num):
	if num % 10 == 0:
		return True
	else:
		return False

def sumElements(list):
	sum = 0
	for elem in list:
		sum = sum + elem
	return sum

isValid(4388576018402626)