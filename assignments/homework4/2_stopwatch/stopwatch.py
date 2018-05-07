import time

class StopWatch:
	def __init__(self, startTime):
		self.__startTime = startTime
		self.__endTime = self.stop() # is that right?

	#accessor methods
	def getStartTime(self):
		return self.__startTime

	def getEndTime(self):
		return self.__endTime

	def start(self):
		self.__startTime = time.time()

	def stop(self):
		self.__endTime = time.time()

	def getElapsedTime(self):
		return self.__endTime - self.__startTime 