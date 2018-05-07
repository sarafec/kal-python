class Stock:
	def __init__(self, symbol, name, previousClosingPrice, currentPrice):
		self.__symbol = symbol
		self.__name	= name
		self.__previousClosingPrice = previousClosingPrice
		self.__currentPrice = currentPrice

	# accessor methods
	def getSymbol(self):
		return self.__symbol

	def getName(self):
		return self.__name

	def getPreviousClosingPrice(self):
		return self.__previousClosingPrice

	def getCurrentPrice(self):
		return self.__currentPrice

	# mutator methods
	def setPreviousClosingPrice(self, price):
		self.__previousClosingPrice = price

	def setCurrentPrice(self, price):
		self.__currentPrice = price

	def getChangePercent(self):
		return ((self.__currentPrice-self.__previousClosingPrice)/self.__previousClosingPrice) * 100