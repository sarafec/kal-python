class Rectangle:
	def __init__(self, height = 2, width = 1):
		self.height = height
		self.width = width

	def getArea(self):
		return self.height * self.width

	def getPerimeter(self):
		return (self.height + self.width) * 2

