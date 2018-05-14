def middle(record):
	symbol, low, high, current = record
	return (low + high)/2

stock = ("MSFT",  80.00, 140.00, 92.05)
print(middle(stock))
print(stock[0:3])