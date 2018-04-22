def sqrt(n):
	if (n < 0):
		print("Please input a positive number.")
		return

	guess = 1

	while True:
		difference = guess**2 - n

		if abs(difference) <= 0.0001:
			break

		guess = (guess + n/guess) / 2

	print (int(guess), "is the square root of", n)


sqrt(-340)