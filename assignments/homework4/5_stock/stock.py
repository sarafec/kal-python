class Stock:
	def __init__(self):
		self.__symbol 					# todo: how to initialize value
		self.__name						# todo: how to initialize value
		self.__previousClosingPrice		# todo: how to initialize value
		self.__currentPrice				# todo: how to initialize value

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
		return (self.__currentPrice/self.__previousClosingPrice) * 100