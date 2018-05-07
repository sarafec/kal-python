import datetime
import math

class Time:
	def __init__(self):
		self.__hour = datetime.datetime.now().hour
		self.__minute = datetime.datetime.now().minute
		self.__second = datetime.datetime.now().second

	def getHour(self):
		return self.__hour

	def getMinute(self):
		return self.__minute

	def getSecond(self):
		return self.__second

	# todo: this feels like a monster method, can we break it up?
	# todo: consider adding a print and format time method to print the current and elapsed time
	def setTime(self, elapsedTime):
		# how many hours exist in elapsedTime
		if elapsedTime >= 3600:
			hours = math.floor(elapsedTime/3600)
			elapsedTime -= 3600 * hours
		# how many minutes in elapsedTime
		if elapsedTime >= 60:
			minutes = math.floor(elapsedTime/60)
			elapsedTime -= 60 * minutes

		self.__hour += hours
		self.__minute += minutes
		self.__second += elapsedTime

		# todo: this doesn't carry over values from the second to the minute, minute to hour
		# todo: consider adding additional methods to handle this functionality
		if self.__hour > 23:
			self.__hour -= 23

		if self.__minute > 59:
			self.__minute -= 59

		if self.__second > 59:
			self.__second -= 59

		return str(math.floor(self.__hour)) + ":" + str(math.floor(self.__minute)) + ":" + str(math.floor(self.__second))
