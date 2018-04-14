import math

def sumAllDigits(num):
	hundreds = 0
	tens = 0
	ones = 0

	if (num == 1000):
		return 1
	if (num >= 100):
		hundreds  = math.floor(num / 100)
		num = num - (hundreds * 100)
	if (num >= 10):
		tens = math.floor(num/10)
		num = num - (tens * 10)
	if (num >= 0):
		ones = num

	print(hundreds + tens + ones)

sumAllDigits(123)
sumAllDigits(5)
sumAllDigits(0)
sumAllDigits(25)