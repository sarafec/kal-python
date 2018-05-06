import time

class StopWatch:
	def __init__(self):
		self.__startTime = time.time()
		self.__endTime = time.time()

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
		startTime = start()
		endTime = stop()
		return endTime - startTime 