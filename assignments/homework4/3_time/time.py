import datetime

class Time:
	def __init__(self):
		self.__hour = datetime.hour()
		self.__minute = datetime.minute()
		self.__second = datetime.second()

	def getHour(self):
		return self.__hour

	def getMinute(self):
		return self.__minute

	def getSecond(self):
		return self.__second

	def setTime(self, elapsedTime):
		# todo: set a new time using the elapsed time