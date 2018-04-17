import math 

def calculateVolume():
	radius = eval(input("Please input radius: "))
	length = eval(input("Please input length: "))

	area = (radius ** 2) * math.pi
	volume = area * length
	print("The volume is ", volume)

calculateVolume()