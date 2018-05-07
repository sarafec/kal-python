class Fan:
	def __init__(self, speed=1, radius=5, fanColor="blue"):
		self.SLOW = 1
		self.MEDIUM = 2
		self.FAST = 3
		self.__speed = speed
		self.__isOn = False
		self.__fanRadius = radius
		self.__fanColor = fanColor

	# accessor methods
	def getFanSpeed(self):
		return self.__speed

	def getFanState(self):
		return self.__isOn

	def getFanRadius(self):
		return self.__fanRadius

	def getFanColor(self):
		return self.__fanColor

	# mutator methods
	def setFanSpeed(self, speed):
		self.__speed = speed

	def setFanState(self, isOn):
		self.__isOn = isOn

	def setFanRadius(self, radius):
		self.__fanRadius = radius

	def setFanColor(self, color):
		self.__fanColor = color