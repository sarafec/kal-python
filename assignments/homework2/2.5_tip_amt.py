def calculateTipAmt():
	subtotal = eval(input("Enter the subtotal: "))
	tipRate = eval(input("Enter the tip rate (as decimal percentage): "))
	tipAmt = subtotal * tipRate
	print(subtotal + tipAmt)

calculateTipAmt()