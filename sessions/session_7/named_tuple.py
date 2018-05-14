from collections import namedtuple
stock = namedtuple("Stock", "symbol current high low")
s1 = stock("MSFT", 92.05, 140.00, 80.00)
s2 = stock("AMZN", 1426.20, 1500.00, 80.00)

stocks = []
stocks.append(s1)
stocks.append(s2)

print(s1.current)
